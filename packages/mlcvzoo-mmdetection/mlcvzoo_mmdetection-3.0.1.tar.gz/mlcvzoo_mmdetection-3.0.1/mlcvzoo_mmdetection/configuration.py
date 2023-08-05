# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Definition of the MMDetectionConfig that is used to configure the MMDetectionModel.
"""

import logging
from typing import Any, Dict, List, Optional

import related
from config_builder.BaseConfigClass import BaseConfigClass
from mlcvzoo_base.api.configuration import Configuration
from mlcvzoo_base.configuration.AnnotationHandlerConfig import AnnotationHandlerConfig
from mlcvzoo_base.configuration.class_mapping_config import ClassMappingConfig
from mlcvzoo_base.configuration.detector_configs import DetectorConfig, InferenceConfig
from mlcvzoo_base.configuration.reduction_mapping_config import ReductionMappingConfig

logger = logging.getLogger(__name__)


@related.mutable(strict=True)
class MMDetectionModelOverwriteConfig(BaseConfigClass):

    num_classes: int = related.IntegerField()

    def check_values(self) -> bool:
        return self.num_classes >= 1


@related.mutable(strict=True)
class MMDetectionTrainArgparseConfig(BaseConfigClass, Configuration):
    # argparse parameter from mmdetection:

    # train config file path
    config: str = related.StringField()
    # the dir to save logs and models
    work_dir: str = related.StringField()
    # the checkpoint file to resume from
    resume_from: str = related.StringField()
    # whether not to evaluate the checkpoint during training
    no_validate: bool = related.BooleanField()
    # whether to set deterministic options for CUDNN backend.
    deterministic: bool = related.BooleanField()
    # random seed
    seed: Optional[int] = related.IntegerField(required=False, default=None)
    # number of gpus to use
    gpus: Optional[int] = related.IntegerField(required=False, default=None)
    # ids of gpus to use
    gpu_ids: Optional[List[int]] = related.ChildField(
        cls=list, required=False, default=None
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

    def check_values(self) -> bool:
        return self.launcher in ["none", "pytorch", "slurm", "mpi"]


@related.mutable(strict=True)
class MMDetectionTrainOverwriteConfig(BaseConfigClass, Configuration):
    # the following parameters are used to overwrite parameters
    # in the config .py files of mmdetection:

    total_epochs: int = related.IntegerField()

    train_ann_file_list: List[str] = related.SequenceField(cls=str)

    val_ann_file_list: List[str] = related.SequenceField(cls=str)

    test_ann_file_list: List[str] = related.SequenceField(cls=str)

    lr_config_steps: List[int] = related.SequenceField(cls=int)

    log_config_interval: int = related.IntegerField()

    samples_per_gpu: int = related.IntegerField()

    workers_per_gpu: int = related.IntegerField()

    train_annotation_handler_config_path: str = related.StringField(default="")
    val_annotation_handler_config_path: str = related.StringField(default="")
    test_annotation_handler_config_path: str = related.StringField(default="")

    train_annotation_handler_config: Optional[
        AnnotationHandlerConfig
    ] = related.ChildField(cls=AnnotationHandlerConfig, required=False, default=None)
    val_annotation_handler_config: Optional[
        AnnotationHandlerConfig
    ] = related.ChildField(cls=AnnotationHandlerConfig, required=False, default=None)
    test_annotation_handler_config: Optional[
        AnnotationHandlerConfig
    ] = related.ChildField(cls=AnnotationHandlerConfig, required=False, default=None)


@related.mutable(strict=True)
class MMDetectionDistributedTrainConfig(BaseConfigClass, Configuration):

    # CUDA device IDs that are visible during the training.
    # This will be used to set the os environment variable: CUDA_VISIBLE_DEVICES
    cuda_visible_devices: str = related.StringField()

    # synchronisation port for interprocess communication
    multi_gpu_sync_port: int = related.IntegerField(default=29500)


@related.mutable(strict=True)
class MMDetectionTrainConfig(BaseConfigClass, Configuration):
    """
    argparse parameter from mmdetection/tools/train.py
    """

    argparse_config: MMDetectionTrainArgparseConfig = related.ChildField(
        cls=MMDetectionTrainArgparseConfig
    )

    multi_gpu_config: Optional[MMDetectionDistributedTrainConfig] = related.ChildField(
        cls=MMDetectionDistributedTrainConfig, required=False, default=None
    )


@related.mutable(strict=True)
class MMDetectionInferenceConfig(InferenceConfig):

    device_string: str = related.StringField(default="cuda:0")

    reduction_class_mapping: Optional[ReductionMappingConfig] = related.ChildField(
        cls=ReductionMappingConfig, required=False, default=None
    )

    def check_values(self) -> bool:
        success: bool = True
        if not 0.0 <= self.score_threshold <= 1.0:
            success = False
        return success


@related.mutable(strict=True)
class MMDetectionConfig(BaseConfigClass, Configuration):

    # NOTE: only the "gpus" OR the "gpu_ids" parameter is used by the mmdetection train routine
    #       therefore make the mutual exclusive in the configuration
    mutual_attribute_map: Dict[str, List[str]] = {
        "MMDetectionTrainArgparseConfig": ["gpus", "gpu_ids"]
    }

    class_mapping: ClassMappingConfig = related.ChildField(cls=ClassMappingConfig)

    inference_config: MMDetectionInferenceConfig = related.ChildField(
        cls=MMDetectionInferenceConfig
    )

    train_config: MMDetectionTrainConfig = related.ChildField(
        cls=MMDetectionTrainConfig
    )

    base_config: DetectorConfig = related.ChildField(
        cls=DetectorConfig, default=DetectorConfig()
    )
