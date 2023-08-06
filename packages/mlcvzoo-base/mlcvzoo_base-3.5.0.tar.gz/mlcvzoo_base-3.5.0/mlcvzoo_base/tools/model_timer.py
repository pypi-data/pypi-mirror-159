# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

import argparse
import logging
import sys
import time
from typing import Dict, List, Optional, cast

import cv2
import mlflow
from config_builder import ConfigBuilder

from mlcvzoo_base.api.model import ConfigurationType, DataType, Model, PredictionType
from mlcvzoo_base.configuration.structs import DeviceQueryTypes, MLFlowExperimentTypes
from mlcvzoo_base.configuration.utils import handle_value_error_for_tool_configuration
from mlcvzoo_base.metrics.mlflow.mlflow_runner import MLFLowRunner
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.tools.configuration.model_timer_config import ModelTimerConfig
from mlcvzoo_base.tools.logger import Logger
from mlcvzoo_base.utils.gpu_util import GpuInfo, get_device_info

logger = logging.getLogger(__name__)


class ModelTimer(ConfigBuilder):
    """
    Utility class for measuring the individual inference time of a group of models specified in the ModelTimer config
    file and logging the results to MLFlow.
    """

    argparse_description: str = (
        "Measure the individual inference time of a group of models specified "
        "in the ModelTimer config file and optionally log the results to MLFlow."
    )

    def __init__(
        self,
        yaml_config_path: Optional[str] = None,
        configuration: Optional[ModelTimerConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ) -> None:
        try:
            config_builder = ConfigBuilder(
                class_type=ModelTimerConfig,
                configuration=configuration,
                yaml_config_path=yaml_config_path,
                argparse_module_description="Tool for logging the runtime of mlcvzoo models",
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
                use_argparse_fallback=True,
            )

            self.configuration: ModelTimerConfig = cast(
                ModelTimerConfig,
                config_builder.configuration,
            )
        except ValueError as value_error:
            handle_value_error_for_tool_configuration(
                value_error=value_error, config_builder_instance=self
            )
            raise value_error

        self.model_registry = ModelRegistry()

        self.mlflow_runner: Optional[MLFLowRunner] = None
        if self.configuration.mlflow_config is not None:
            self.mlflow_runner = MLFLowRunner(
                configuration=self.configuration.mlflow_config,
            )
        else:
            logger.info(
                "Not able to create MLFLowRunner since no MLFlowConfig was set in ModelTimerConfig.mlflow_config. "
                "Just logging execution time information to standard output."
            )

        self.inference_time_mean: Optional[float] = None
        self.inference_time_list: List[float] = []

    @staticmethod
    def setup_argparse() -> argparse.ArgumentParser:
        """
        Parse command line arguments.

        Returns:
            The argument parser filled with command line arguments
        """
        return ConfigBuilder._setup_argparse(
            argparse_module_description=ModelTimer.argparse_description,
            add_argparse_parameters=ModelTimer._add_argparse_parameters,
        )

    def run(self) -> None:
        """
        Run the models specified in the ModelTimer config file, measure their inference time and log the results
        (inference time based on epoch time and bare process time as well as their means) to MLFlow.
        """

        image = cv2.imread(self.configuration.test_image_path)

        for model_config in self.configuration.model_configs:
            model: Model[PredictionType, ConfigurationType, DataType]  # type: ignore
            model = self.model_registry.init_model(
                model_config=model_config,
                string_replacement_map=self.configuration.string_replacement_map,
            )

            if self.mlflow_runner is not None:
                self.mlflow_runner.start_mlflow_run(
                    experiment_name=MLFlowExperimentTypes.TIMING,
                    run_name=model.get_name(),
                )

                logger.info("Log mlflow metrics for model '%s'", model.__class__)

            # TODO: Use the interface method in future implementations that state
            #       whether the model is running on gpu or cpu
            # mlflow.log_param(key="device_type", value="TODO")

            gpu_info: Optional[GpuInfo] = get_device_info(
                device_query=self.configuration.device_query,
            )

            if gpu_info is not None:
                # log gpu info to mlflow
                mlflow.log_param(key="device_name", value=gpu_info.name)

            # perform warm-up
            for _ in range(0, self.configuration.number_of_warm_up_runs):
                start_epoch_time = time.time_ns()

                model.predict(data_item=image)

                logger.info(f"warm-up-time: {time.time_ns() - start_epoch_time}ms")

            # perform benchmarked inference
            for run_index in range(0, self.configuration.number_of_runs):
                start_epoch_time = time.time_ns()

                model.predict(data_item=image)

                self.inference_time_list.append(
                    (time.time_ns() - start_epoch_time) / 1000 / 1000
                )

                if self.mlflow_runner is not None:
                    mlflow.log_metric(
                        key="runtime_ms",
                        value=self.inference_time_list[-1],
                        step=run_index,
                    )

                logger.info(f"runtime: {self.inference_time_list[-1]}ms")

            if len(self.inference_time_list) > 0:
                self.inference_time_mean = sum(self.inference_time_list) / len(
                    self.inference_time_list
                )

                logger.info(f"runtime-mean: {self.inference_time_mean}ms")

                if self.mlflow_runner is not None:
                    mlflow.log_metric("runtime-mean_ms", value=self.inference_time_mean)
                    self.mlflow_runner.end_run()


def main() -> None:
    """
    Entry point when using the mlcvzoo-modeltimer command line tool.
    (See [tool.poetry.scripts] section in pyproject.toml)
    """

    args = ModelTimer.setup_argparse().parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="ModelTimer",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    try:
        model_timer = ModelTimer()
        model_timer.run()
    except ValueError as value_error:
        if (
            str(value_error) != "Cannot build a config. "
            "Both, the configuration object and yaml_config_path are None"
        ):
            raise value_error
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
