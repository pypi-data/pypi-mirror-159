# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for defining the model classes that are used to wrap the mmocr framework.
"""

import copy
import importlib
import logging
import os
import shlex
import subprocess
import sys
import typing
from abc import ABC
from json import dumps
from statistics import mean
from time import time
from typing import Any, Dict, Generic, List, Optional, Tuple, TypeVar, Union

import mlflow
import torch.nn
from config_builder.replacement_map import get_replacement_map_copy
from mlcvzoo_base.api.data.class_identifier import ClassIdentifier
from mlcvzoo_base.api.data.ocr_perception import OCRPerception
from mlcvzoo_base.api.data.segmentation import PolygonType, Segmentation
from mlcvzoo_base.api.interfaces import NetBased, Trainable
from mlcvzoo_base.api.model import Model, OCRModel, SegmentationModel
from mlcvzoo_base.configuration.replacement_config import ReplacementConfig
from mlcvzoo_base.configuration.utils import (
    create_configuration as create_basis_configuration,
)
from mlcvzoo_mmdetection.utils import init_mmdetection_config
from mmcv.utils import Registry
from mmocr.apis import init_detector
from mmocr.apis.inference import model_inference
from mmocr.datasets import build_dataset  # noqa: F401
from mmocr.models import build_detector  # noqa: F401
from mmocr.models.builder import DETECTORS as mmocr_models
from nptyping import Int, NDArray, Shape

from mlcvzoo_mmocr.configuration import MMOCRConfig
from mlcvzoo_mmocr.utils import get_mmocr_argparse_list

logger = logging.getLogger(__name__)


#################################
# TODO: This is only a workaround and should be fixed by mmdetection or mmocr
mmocr_models.module_dict.update(mmocr_models.parent.module_dict)
#################################

ImageType = NDArray[Shape["Height, Width, Any"], Int]

ModelType = TypeVar(
    "ModelType",
    OCRModel[MMOCRConfig, Union[str, ImageType]],
    SegmentationModel[MMOCRConfig, Union[str, ImageType]],
)


class MMOCRModel(
    Model,  # type: ignore
    NetBased[torch.nn.Module],
    Trainable,
    ABC,
    Generic[ModelType],
):
    """
    Super class for defining shared methods that are used in a MMOCRTextDetectionModel and
    MMOCRTextRecognitionModel.


    NOTE: The constructor of the super class Model will not be called since
          the ReadFromFileModel is an abstract super class and therefore is
          not intended to be instantiated. But make sure to call the Model
          constructor in one of the implementing subclasses.
    """

    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[MMOCRConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        init_for_inference: bool = False,
        is_multi_gpu_instance: bool = False,
    ) -> None:
        self.net: Optional[torch.nn.Module] = None

        self.yaml_config_path: Optional[str] = from_yaml
        self.is_multi_gpu_instance: bool = is_multi_gpu_instance

        self.configuration: MMOCRConfig = MMOCRModel.create_configuration(
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
        )

        Model.__init__(
            self,
            unique_name=self.configuration.base_config.MODEL_SPECIFIER,
            configuration=self.configuration,
        )

        if init_for_inference:
            self.__initialize_net()

        NetBased.__init__(self, net=self.net)

    def get_net(self) -> Optional[torch.nn.Module]:
        return self.net

    def __initialize_net(self) -> None:

        cfg, self.configuration.inference_config.config_path = init_mmdetection_config(
            config_path=self.configuration.inference_config.config_path,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        cfg.merge_from_dict(self.configuration.train_config.argparse_config.cfg_options)

        logger.info(
            "Load model for %s from %s",
            self.get_name(),
            self.configuration.inference_config.checkpoint_path,
        )

        self.net = init_detector(
            config=cfg,
            checkpoint=self.configuration.inference_config.checkpoint_path,
            device=self.configuration.inference_config.device_string,
        )

    @staticmethod
    def create_configuration(
        from_yaml: Optional[str] = None,
        configuration: Optional[MMOCRConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
    ) -> MMOCRConfig:
        return typing.cast(
            MMOCRConfig,
            create_basis_configuration(
                configuration_class=MMOCRConfig,
                from_yaml=from_yaml,
                input_configuration=configuration,
                string_replacement_map=string_replacement_map,
            ),
        )

    @staticmethod
    def __register_dataset() -> None:
        """
        Register the custom dataset "SegmentationDataset" of the MLCVZoo in the registry of mmcv

        Returns:
            None
        """

        # NOTE: DO NOT REMOVE THIS IMPORT
        from mlcvzoo_mmocr.segmentation_dataset import SegmentationDataset

        DATASETS = Registry("dataset")
        DATASETS.register_module("SegmentationDataset")

    @staticmethod
    def run_mmocr_train(mmocr_dir: str) -> None:
        """
        Call training script of the mmocr repository. Since the tools package is
        not part of their sources, it has to be called utilizing importlib python package

        Args:
            mmocr_dir: Path to the mmocr repository

        Returns:
            None

        """

        MMOCRModel.__register_dataset()

        module_name = "train"

        # Clear module import
        if module_name in sys.modules:
            del sys.modules[module_name]

        mmocr_train_module_dir = os.path.join(mmocr_dir, "tools")

        logger.info("Load mmdet train module from path: %s", mmocr_train_module_dir)

        sys_path_copy = copy.deepcopy(sys.path)
        # Set PYTHONPATH to only contain the relevant directory for the importlib call
        sys.path = [mmocr_train_module_dir]

        mmocr_train_module = importlib.import_module(module_name)

        # Revert modifications to the PYTHONPATH
        sys.path = sys_path_copy

        # Run the mmdet training
        mmocr_train_module.main()

    @staticmethod
    def __set_string_replacement_dict_in_cfg(
        cfg_options: Optional[Dict[str, Any]], string_replacement_map: Dict[str, str]
    ) -> Optional[Dict[str, Any]]:
        """
        Takes a dictionary representing the train_config.cfg_options of the MMDetectionConfig
        and sets the data.{train_step}.string_replacement_map_string_list if a
        data.{train_step}.annotation_handler_config_path is present. This is needed in order
        to make the string replacement available in the SegmentationDataset that the MLCVZoo adds
        to the mmocr/mmdetection framework.

        Returns:
            The modified cfg_options dictionary
        """

        train_steps = ["train", "val", "test"]

        for train_step in train_steps:
            if (
                cfg_options is not None
                and f"data.{train_step}.annotation_handler_config_path"
            ):
                # TODO: add string_replacement json string
                cfg_options[
                    f"data.{train_step}.string_replacement_map_string_list"
                ] = "".join(dumps(string_replacement_map))

        return cfg_options

    def __run_training(self, mmocr_dir: str) -> None:
        """
        Run mmocr training.

        Args:
            mmocr_dir: Directory where the mmocr repository has been cloned to.
                       This is needed to be able to call there tools/train.py script.

        Returns:
            None
        """

        argparse_config = self.configuration.train_config.argparse_config

        _, new_config_path = init_mmdetection_config(
            config_path=argparse_config.config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        self.__set_string_replacement_dict_in_cfg(
            cfg_options=argparse_config.cfg_options,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        if argparse_config.launcher == "none":
            argv_list = [
                sys.argv[0],
                new_config_path,
            ]
        else:
            argv_list = sys.argv.copy()

        argv_list.extend(
            get_mmocr_argparse_list(
                argparse_config=argparse_config,
                string_replacement_map=self.configuration.string_replacement_map,
            )
        )

        logger.info("Set sys.argv to: %s", sys.argv)

        sys.argv = argv_list

        MMOCRModel.run_mmocr_train(mmocr_dir=mmocr_dir)

        mlflow.end_run()

    def __run_multi_gpu_training(self, mmocr_dir: str) -> None:
        """
        Run mmocr multi-gpu/distributed training.

        Args:
            mmocr_dir: Directory where the mmocr repository has been cloned to.
                       This is needed to be able to call there tools/train.py script.

        Returns:
            None
        """

        assert self.configuration.train_config.multi_gpu_config is not None

        cuda_visible_devices = (
            self.configuration.train_config.multi_gpu_config.cuda_visible_devices
        )
        gpus = self.configuration.train_config.argparse_config.gpus
        port = self.configuration.train_config.multi_gpu_config.multi_gpu_sync_port

        env = os.environ.copy()
        env[
            "PYTHONPATH"
        ] = f"{os.environ.get('PYTHONPATH') if os.environ.get('PYTHONPATH') is not None else ''}"
        env["PYTHONPATH"] += f":{mmocr_dir}"

        env["cuda_visible_devices"] = cuda_visible_devices

        for key, value in get_replacement_map_copy().items():
            env[key] = value

        _, new_config_path = init_mmdetection_config(
            config_path=self.configuration.train_config.argparse_config.config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        self.configuration.train_config.argparse_config.cfg_options = (
            self.__set_string_replacement_dict_in_cfg(
                cfg_options=self.configuration.train_config.argparse_config.cfg_options,
                string_replacement_map=self.configuration.string_replacement_map,
            )
        )

        argv_list = get_mmocr_argparse_list(
            argparse_config=self.configuration.train_config.argparse_config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        command = (
            f"-m torch.distributed.run "
            f"--nproc_per_node={gpus} "
            f"--master_port={port} "
            f"{__file__} "
            f"{new_config_path} "
        )

        for argv_parameter in argv_list:
            command += str(argv_parameter) + " "

        command += f"{mmocr_dir} "

        command_split = [sys.executable]
        command_split.extend(shlex.split(command))
        logger.debug("Run command: %s", " ".join(command_split))
        result = subprocess.run(command_split, env=env, stdout=sys.stdout)

        if result.returncode:
            logger.error(
                "Command '%s' returned with exit code %i", command, result.returncode
            )
            raise RuntimeError(
                f"Distributed training excited with exitcode != 0, "
                f"exitcode: {result.returncode}"
            )

    def train(self) -> None:

        if (
            ReplacementConfig.MMOCR_DIR_KEY
            not in self.configuration.string_replacement_map
        ):
            raise ValueError(
                f"Please provide a valid value "
                f"for the key '{ReplacementConfig.MMOCR_DIR_KEY}' "
                f"in your replacement configuration file."
            )

        mmocr_dir = self.configuration.string_replacement_map[
            ReplacementConfig.MMOCR_DIR_KEY
        ]

        if self.configuration.train_config.argparse_config.launcher == "none":
            self.__run_training(mmocr_dir=mmocr_dir)
        else:
            self.__run_multi_gpu_training(mmocr_dir=mmocr_dir)

    def _predict(
        self,
        data_item: Union[Union[str, ImageType], List[Union[str, ImageType]]],
    ) -> Any:

        start = time()
        results = model_inference(model=self.net, imgs=data_item)
        end = time() - start

        logger.debug(
            "MMOCRTextRecognitionModel '%s' prediction time: %.4f | result: %s",
            self.get_name(),
            end,
            results,
        )

        return results


class MMOCRTextDetectionModel(
    SegmentationModel[MMOCRConfig, Union[str, ImageType]],
    MMOCRModel[
        SegmentationModel[MMOCRConfig, Union[str, ImageType]],
    ],
):
    text_class_id: int = 0
    text_class_name: str = "text"

    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[MMOCRConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        init_for_inference: bool = False,
        is_multi_gpu_instance: bool = False,
    ) -> None:

        MMOCRModel.__init__(
            self,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
            init_for_inference=init_for_inference,
            is_multi_gpu_instance=is_multi_gpu_instance,
        )
        SegmentationModel.__init__(
            self,
            unique_name=self.configuration.base_config.MODEL_SPECIFIER,
            configuration=self.configuration,
        )

    @property
    def num_classes(self) -> int:
        # This Segmentation models should only detect text snippets in an image,
        # therefore it only has the one class "text"
        return 1

    def get_classes_id_dict(self) -> Dict[int, str]:
        # This model only detects text segmentations, therefore is has a static class mapping
        return {
            MMOCRTextDetectionModel.text_class_id: MMOCRTextDetectionModel.text_class_name
        }

    @staticmethod
    def __decode_mmocr_result_to_list_of_points(
        text_detection_result: List[float],
    ) -> PolygonType:
        """
        Converts MMOCR result to list of tuples. MMOCR stores the result as
        [x,y,x,y,x,y,x,y, ..., score]. This function takes all but the last
        element (the score) of the MMOCR result and reshapes them.
        The returned format is [(x, y), (x, y), ...].
        """

        # we skip last entry because this is a confidence value
        return list(zip(text_detection_result[:-1:2], text_detection_result[1:-1:2]))

    def __process_text_detection_result(
        self, result: Dict[str, Any]
    ) -> List[Segmentation]:

        segmentations: List[Segmentation] = list()

        for text_detection_result in result["boundary_result"]:
            score: float = text_detection_result[-1]

            polygon: PolygonType = (
                MMOCRTextDetectionModel.__decode_mmocr_result_to_list_of_points(
                    text_detection_result=text_detection_result
                )
            )

            if score >= self.configuration.inference_config.score_threshold:
                segmentations.extend(
                    self.build_segmentations(
                        class_identifiers=[
                            ClassIdentifier(
                                class_id=self.text_class_id,
                                class_name=self.text_class_name,
                            )
                        ],
                        score=score,
                        polygon=polygon,
                    )
                )

                if self.configuration.inference_config.to_rect_polygon:
                    for segmentation in segmentations:
                        segmentation.to_rect_polygon()

        return segmentations

    def predict(
        self, data_item: Union[str, ImageType]
    ) -> Tuple[Union[str, ImageType], List[Segmentation]]:

        assert self.net is not None

        return data_item, self.__process_text_detection_result(
            result=self._predict(data_item=data_item)
        )

    def predict_many(
        self, data_items: List[Union[str, ImageType]]
    ) -> List[Tuple[Union[str, ImageType], List[Segmentation]]]:

        assert self.net is not None

        prediction_list: List[Tuple[Union[str, ImageType], List[Segmentation]]] = []

        results = self._predict(data_item=data_items)

        for data_item, result in zip(data_items, results):

            segmentations = self.__process_text_detection_result(result=result)

            prediction_list.append(
                (
                    data_item,
                    segmentations,
                )
            )

        return prediction_list


class MMOCRTextRecognitionModel(
    OCRModel[MMOCRConfig, Union[str, ImageType]],
    MMOCRModel[
        OCRModel[MMOCRConfig, Union[str, ImageType]],
    ],
):
    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[MMOCRConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        init_for_inference: bool = False,
        is_multi_gpu_instance: bool = False,
    ) -> None:
        MMOCRModel.__init__(
            self,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
            init_for_inference=init_for_inference,
            is_multi_gpu_instance=is_multi_gpu_instance,
        )
        OCRModel.__init__(
            self,
            unique_name=self.configuration.base_config.MODEL_SPECIFIER,
            configuration=self.configuration,
        )

    def __process_result(self, result: Dict[str, Any]) -> Optional[OCRPerception]:

        if isinstance(result["score"], list):
            score = mean(result["score"])
        else:
            score = result["score"]

        if score >= self.configuration.inference_config.score_threshold:
            return OCRPerception(content=result["text"], score=score)

        return None

    def predict(
        self, data_item: Union[str, ImageType]
    ) -> Tuple[Union[str, ImageType], List[OCRPerception]]:

        assert self.net is not None

        ocr_texts: List[OCRPerception] = []

        ocr_perception = self.__process_result(
            result=self._predict(data_item=data_item)
        )

        if ocr_perception is not None:
            ocr_texts.append(ocr_perception)

        return data_item, ocr_texts

    def predict_many(
        self, data_items: List[Union[str, ImageType]]
    ) -> List[Tuple[Union[str, ImageType], List[OCRPerception]]]:

        assert self.net is not None

        prediction_list: List[Tuple[Union[str, ImageType], List[OCRPerception]]] = []

        results = self._predict(data_item=data_items)

        for data_item, result in zip(data_items, results):

            ocr_perception = self.__process_result(result=result)

            if ocr_perception is not None:

                prediction_list.append(
                    (
                        data_item,
                        [ocr_perception],
                    )
                )
            else:
                prediction_list.append(
                    (
                        data_item,
                        [],
                    )
                )

        return prediction_list
