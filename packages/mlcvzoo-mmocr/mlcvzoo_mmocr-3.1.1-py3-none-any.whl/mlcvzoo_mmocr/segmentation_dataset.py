# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for providing the possibility to train a mmocr
model on data that is provided by the annotation handler
of the MLCVZoo. This is realized by extending the 'DATASETS'
registry of mmocr (mmdetection).
"""

import logging
from typing import Any, Dict, List, Optional

import numpy as np
from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.configuration.AnnotationHandlerConfig import AnnotationHandlerConfig
from mlcvzoo_base.data_preparation.AnnotationHandler import AnnotationHandler
from mlcvzoo_base.evaluation.object_detection.utils import generate_img_id_map
from mlcvzoo_mmdetection.utils import parse_string_replacement_map
from mmdet.datasets.builder import DATASETS
from mmdet.datasets.custom import CustomDataset

logger = logging.getLogger(__name__)


@DATASETS.register_module()
class SegmentationDataset(CustomDataset):
    """
    Implementation of a custom dataset. It follows the instructions given by:
    https://mmdetection.readthedocs.io/en/latest/tutorials/customize_dataset.html

    We followed an example and created our own dataset class
    which has to be compatible to the class "CustomDataset"
    of the mmdetection framework

    Custom dataset for segmentations.

    Annotation format required from mmdet.datasets.custom.CustomDataset:
    [
        {
            'filename': 'a.jpg',
            'width': 1280,
            'height': 720,
            'ann': {
                'bboxes': <np.ndarray> (n, 4),
                'labels': <np.ndarray> (n, ),
                'bboxes_ignore': <np.ndarray> (k, 4), (optional field) => NOTE: not yet implemented
                'labels_ignore': <np.ndarray> (k, 4) (optional field)  => NOTE: not yet implemented
            }
        },
        ...
    ]

    The `ann` field is optional for testing.
    """

    def __init__(  # pylint: disable=R0913, disable=R0914
        self,  # pylint: disable=W0613
        ann_file: Optional[
            str
        ],  # => ensure compatibility to superclass 'CustomDataset'
        pipeline: Optional[Any],
        classes: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        data_root: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        img_prefix: Optional[
            str
        ] = "",  # => ensure compatibility to superclass 'CustomDataset'
        seg_prefix: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        proposal_file: Optional[
            Any
        ] = None,  # => ensure compatibility to superclass 'CustomDataset'
        test_mode: bool = False,  # => ensure compatibility to superclass 'CustomDataset'
        filter_empty_gt: bool = True,  # => ensure compatibility to superclass 'CustomDataset'
        annotation_handler_config_path: str = "",
        annotation_handler_config: Optional[AnnotationHandlerConfig] = None,
        string_replacement_map_string_list: Optional[List[str]] = None,
        datasets: Optional[Any] = None,  # pylint: disable=W0613
        separate_eval: bool = True,  # pylint: disable=W0613
        show_mean_scores: str = "auto",  # pylint: disable=W0613
        force_apply: bool = False,  # pylint: disable=W0613
        **kwargs: Any  # pylint: disable=W0613
    ) -> None:
        # NOTE: The unused parameter above are necessary in order for mmdet to use this Dataset

        self.annotations: List[BaseAnnotation] = []

        string_replacement_map: Dict[str, str] = {}
        if string_replacement_map_string_list is not None:
            string_replacement_map = parse_string_replacement_map(
                string_replacement_map_string_list=string_replacement_map_string_list
            )

        self.annotation_handler = AnnotationHandler(
            yaml_config_path=annotation_handler_config_path,
            configuration=annotation_handler_config,
            string_replacement_map=string_replacement_map,
        )

        CustomDataset.__init__(
            self,
            ann_file=ann_file,
            pipeline=pipeline,
            classes=None,
            data_root=None,
            img_prefix="",
            seg_prefix=None,
            proposal_file=None,
            test_mode=False,
            filter_empty_gt=True,
        )

        self.flag = np.ones(len(self), dtype=np.uint8)

        self.CLASSES = self.annotation_handler.mapper.get_model_class_names()

        logger.info("Finished SegmentationDataset init ...")

        self.img_directory_id_dict: Dict[str, int] = {}

    def __len__(self):  # type: ignore
        return len(self.data_infos)

    def load_annotations(self, ann_file) -> List:  # type: ignore
        """
        Overwrite from 'CustomDataset'.

        Parse all annotation data from the configured csv-files and save it to a Dict
        which is in the 'CustomDataset' format

        Args:
            ann_file: currently not used. Annotation is loaded through the AnnotationHandler
                Therefore, annotation location can be specified in AnnotationHandlerConfig

        Returns:
            A List of Image information (size, location) in CustimDataset fromat

        """

        img_infos = []

        self.annotations = self.annotation_handler.parse_from_all_source()

        remove_indices: List[int] = []

        for index, annotation in enumerate(self.annotations):

            if len(annotation.segmentations) == 0:
                remove_indices.append(index)

        # The indices have to be in reverse order because pop changes the
        # length of the list. Therefore, we have to start from the back
        remove_indices.sort(reverse=True)

        for index in remove_indices:
            remove_annotation = self.annotations.pop(index)
            logger.info(
                "Removing annotation from list, because it does not contain any segmentations!\n"
                "  - annotation.image_path: %s\n"
                "  - annotation.segmentations: %s\n"
                "  - annotation.bounding_boxes: %s\n"
                "  - annotation.all_bounding_boxes: %s",
                remove_annotation.image_path,
                remove_annotation.segmentations,
                remove_annotation.bounding_boxes,
                remove_annotation.get_bounding_boxes(include_segmentations=True),
            )

        for _, annotation in enumerate(self.annotations):

            # Dict structure is based on 'CustomDataset'
            info = dict(
                height=annotation.get_height(),
                width=annotation.get_width(),
                filename=annotation.image_path,
            )

            img_infos.append(info)

        return img_infos

    def get_ann_info(self, idx: int) -> Dict[str, Any]:
        """
        Overwrite from 'CustomDataset' to get the annotations for mmdetection in the correct format

        """

        gt_labels: List[int] = []
        gt_bboxes: List[List[float]] = []
        gt_bboxes_ignore: np.ndarray = np.zeros((0, 4), dtype=np.float32)  # type: ignore[type-arg]
        gt_masks_ann: List[Optional[List[List[float]]]] = []
        gt_masks_ignore: List[Optional[List[List[float]]]] = []

        annotation = self.annotations[idx]
        logger.debug(
            "Load annotation via get_ann_info for index %s: \n"
            "  - annotation.image_path: %s\n"
            "  - annotation.segmentations: %s\n"
            "  - annotation.bounding_boxes: %s\n"
            "  - annotation.all_bounding_boxes: %s\n",
            idx,
            annotation.image_path,
            annotation.segmentations,
            annotation.bounding_boxes,
            annotation.get_bounding_boxes(include_segmentations=True),
        )

        # TODO: use also bounding-box or only segmentations?
        # for bounding_box in annotation.get_bounding_boxes(include_segmentations=False):
        #     if bounding_box.box is not None and annotation.is_valid_bounding_box(
        #         box=bounding_box.box
        #     ):
        #
        #         gt_labels.append(bounding_box.class_id)
        #         gt_bboxes.append(bounding_box.box.to_list(dst_type=float))
        #         gt_masks_ann.append(None)
        #     else:
        #         logger.warning(
        #             "Skip bounding-box because it doesn't fulfill "
        #             f"the requirements check by is_valid_bounding_box: \n"
        #             f"  - annotation.image_path: {annotation.image_path}\n"
        #             f"  - bounding-box: {bounding_box}"
        #         )

        for segmentation in annotation.segmentations:
            if segmentation.box is not None and annotation.is_valid_bounding_box(
                box=segmentation.box
            ):

                gt_labels.append(segmentation.class_id)
                gt_bboxes.append(segmentation.box.to_list(dst_type=float))
                gt_masks_ann.append(segmentation.to_list(dst_type=float))
            else:
                annotation_index, self.img_directory_id_dict = generate_img_id_map(
                    image_path=annotation.image_path,
                    img_directory_id_dict=self.img_directory_id_dict,
                )

                logger.warning(
                    "Skip segmentation because the surround box doesn't fulfill "
                    "the requirements check by is_valid_bounding_box: \n"
                    "  - annotation.image_path: %s\n"
                    "  - segmentation: %s\n"
                    "  - annotation-index: %s",
                    annotation.image_path,
                    segmentation,
                    annotation_index,
                )

        if len(gt_bboxes) > 0:
            gt_labels_np = np.array(gt_labels, dtype=np.int64)
            gt_bboxes_np = np.array(gt_bboxes, dtype=np.float32)
        else:
            annotation_index, self.img_directory_id_dict = generate_img_id_map(
                image_path=annotation.image_path,
                img_directory_id_dict=self.img_directory_id_dict,
            )

            logger.warning(
                "No ground-truth bounding-boxes are given: "
                "  - annotation.image_path: %s\n"
                "  - annotation-index: %s\n"
                "  - annotation.segmentations: %s"
                "  - annotation.bounding_boxes: %s"
                "  - annotation.all_bounding_boxes: %s",
                annotation.image_path,
                annotation_index,
                annotation.segmentations,
                annotation.bounding_boxes,
                annotation.get_bounding_boxes(include_segmentations=True),
            )
            gt_labels_np = np.array([], dtype=np.int64)
            gt_bboxes_np = np.zeros((0, 4), dtype=np.float32)

        seg_map = annotation.image_path

        ann: Dict[str, Any] = dict(
            labels=gt_labels_np,
            bboxes=gt_bboxes_np,
            bboxes_ignore=gt_bboxes_ignore,
            masks=gt_masks_ann,
            masks_ignore=gt_masks_ignore,
            seg_map=seg_map,
        )

        return ann
