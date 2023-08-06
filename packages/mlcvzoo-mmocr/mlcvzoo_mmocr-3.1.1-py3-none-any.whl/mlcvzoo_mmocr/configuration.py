# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Definition of the MMOCRConfig that is used to configure the MMOCRModel (and subclasses).
"""

import logging
from typing import Any, Dict, List, Optional

import related
from config_builder.BaseConfigClass import BaseConfigClass
from mlcvzoo_base.api.configuration import Configuration
from mlcvzoo_base.configuration.detector_configs import DetectorConfig
from mlcvzoo_base.configuration.replacement_config import ReplacementConfig
from mlcvzoo_mmdetection.configuration import MMDetectionDistributedTrainConfig

logger = logging.getLogger(__name__)


@related.mutable(strict=True)
class MMOCRTrainArgparseConfig(BaseConfigClass, Configuration):
    # argparse parameter from mmdetection:

    # train config file path
    config: str = related.StringField()
    # the dir to save logs and models
    work_dir: str = related.StringField()
    # The checkpoint file to load from.
    load_from: str = related.StringField()
    # whether not to evaluate the checkpoint during training
    no_validate: bool = related.BooleanField()
    # random seed
    seed: int = related.IntegerField()
    # whether to set deterministic options for CUDNN backend.
    deterministic: bool = related.BooleanField()
    # the checkpoint file to resume from
    resume_from: Optional[str] = related.StringField(required=False, default=None)
    # number of gpus to use
    gpus: Optional[int] = related.IntegerField(required=False, default=None)
    # ids of gpus to use (only applicable to non-distributed training).
    gpu_ids: Optional[List[int]] = related.SequenceField(
        cls=int, required=False, default=None
    )
    # override some settings in the used config, the key-value pair '
    # 'in xxx=yyy format will be merged into config file (deprecate), '
    # 'change to --cfg-options instead.
    options: Optional[Dict[str, Any]] = related.ChildField(
        cls=dict, default=None, required=False
    )
    # override some settings in the used config, the key-value pair '
    # 'in xxx=yyy format will be merged into config file. If the value to '
    # 'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
    # 'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
    # 'Note that the quotation marks are necessary and that no white space '
    # 'is allowed.
    cfg_options: Optional[Dict[str, Any]] = related.ChildField(
        cls=dict, default=None, required=False
    )
    # job launcher
    launcher: str = related.StringField(default="none")
    # Memory cache config for image loading speed-up during training.
    mc_config: Optional[str] = related.StringField(required=False, default=None)

    # NOTE: The following argparse arguments from mmdet.tools.train will not be used in this
    #       configuration.
    #
    # - local_rank: int = related.StringField(default=0) rank for distributed training

    def check_values(self) -> bool:
        return self.launcher in ["none", "pytorch", "slurm", "mpi"]


@related.mutable(strict=True)
class MMOCRInferenceConfig(BaseConfigClass):

    config_path: str = related.StringField()
    checkpoint_path: str = related.StringField()

    # whether or not the output polygon should be formatted to represent a rect, or
    # the polygon should be kept as it is
    to_rect_polygon: bool = related.BooleanField(default=False, required=False)

    score_threshold: float = related.FloatField(default=0.3)
    device_string: str = related.StringField(default="cuda:0")

    def check_values(self) -> bool:
        return 0.0 <= self.score_threshold <= 1.0


@related.mutable(strict=True)
class MMOCRTrainConfig(BaseConfigClass, Configuration):
    """
    argparse parameter from mmdetection/tools/train.py
    """

    argparse_config: MMOCRTrainArgparseConfig = related.ChildField(
        cls=MMOCRTrainArgparseConfig
    )

    multi_gpu_config: Optional[MMDetectionDistributedTrainConfig] = related.ChildField(
        cls=MMDetectionDistributedTrainConfig, required=False, default=None
    )


@related.mutable(strict=True)
class MMOCRConfig(BaseConfigClass, Configuration):
    # NOTE: only the "gpus" OR the "gpu_ids" parameter is used by the mmdetection train routine
    #       therefore make them mutual exclusive in the configuration
    mutual_attribute_map: Dict[str, List[str]] = {}

    inference_config: MMOCRInferenceConfig = related.ChildField(
        cls=MMOCRInferenceConfig
    )

    train_config: MMOCRTrainConfig = related.ChildField(cls=MMOCRTrainConfig)

    base_config: DetectorConfig = related.ChildField(
        cls=DetectorConfig, default=DetectorConfig()
    )
