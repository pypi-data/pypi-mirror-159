# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for handling utility methods that are used across the
mlcvzoo_mmocr package.
"""

import logging
from typing import Any, Dict, List

from mlcvzoo_mmdetection.utils import run_str_string_replacement
from pkg_resources import parse_version

from mlcvzoo_mmocr.configuration import MMOCRTrainArgparseConfig

logger = logging.getLogger(__name__)


def get_mmocr_argparse_list(
    argparse_config: MMOCRTrainArgparseConfig,
    string_replacement_map: Dict[str, str],
) -> List[str]:
    """
    Transform the configuration object into a list of commandline parameters that
    the train function of the mmocr framework understands. Apply string replacements
    in string attributes using the given string_replacement_map

    Args:
        argparse_config: The configuration object to transform
        string_replacement_map: Dictionary used for string replacements

    Returns:
        The list of commandline parameters
    """
    argv_list = [
        "--work-dir",
        argparse_config.work_dir,
        "--load-from",
        argparse_config.load_from,
    ]

    if argparse_config.resume_from is not None:
        argv_list.append("--resume-from")
        argv_list.append(argparse_config.resume_from)

    if argparse_config.mc_config is not None:
        # Only import mmocr when needed
        import mmocr  # pylint: disable=C0415

        mmocr_version = mmocr.__version__
        if parse_version(mmocr_version) <= parse_version("0.4.0"):
            argv_list.append("--mc-config")
            argv_list.append(argparse_config.mc_config)
        else:
            logger.warning(
                "(DEPRECATED) mmocr version='%s' "
                "no longer supports the --mc-config commandline parameter"
                % mmocr_version
            )

    if argparse_config.no_validate:
        argv_list.append("--no-validate")

    if argparse_config.deterministic:
        argv_list.append("--deterministic")

    if argparse_config.seed is not None:
        argv_list.extend(
            [
                "--seed",
                str(argparse_config.seed),
            ]
        )

    if argparse_config.launcher == "none" and argparse_config.gpu_ids is not None:
        gpu_ids = ", ".join([str(gpu_id) for gpu_id in argparse_config.gpu_ids])

        argv_list.extend(
            [
                "--gpu-ids",
                gpu_ids,
            ]
        )

    if argparse_config.cfg_options is not None:
        argv_list.append("--cfg-options")

        cfg_options_dict: Dict[str, Any] = argparse_config.cfg_options

        # TODO: allow that string replacement is executed for dict types in the config-builder
        for config_key, config_value in cfg_options_dict.items():

            if "string_replacement_map_string" not in config_key:
                if isinstance(config_value, str):
                    config_value = run_str_string_replacement(
                        input_string=config_value,
                        string_replacement_map=string_replacement_map,
                    )
                elif isinstance(config_value, list):
                    new_list = []

                    for element in config_value:
                        if type(element) == str:
                            new_element = run_str_string_replacement(
                                input_string=element,
                                string_replacement_map=string_replacement_map,
                            )
                        else:
                            new_element = element

                        new_list.append(new_element)

                    config_value = new_list

            cfg_option = f"{config_key}='{config_value}'"

            argv_list.append(cfg_option)

    return argv_list
