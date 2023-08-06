# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for handling the generation and uploading of annotations that can
be used to pre-annotate annotation tasks
"""

import argparse
import logging
import os
import sys
import zipfile
from typing import Dict, List, Optional, Tuple, cast

import cv2
from config_builder import ConfigBuilder
from tqdm import tqdm

from mlcvzoo_base.api.data.annotation import BaseAnnotation
from mlcvzoo_base.api.model import ConfigurationType, DataType, ObjectDetectionModel
from mlcvzoo_base.configuration.utils import handle_value_error_for_tool_configuration
from mlcvzoo_base.data_preparation.cvat_annotation_handler.cvat_annotation_handler import (
    CVATAnnotationHandler,
)
from mlcvzoo_base.data_preparation.utils import annotation_to_xml
from mlcvzoo_base.models.model_registry import ModelRegistry
from mlcvzoo_base.tools.configuration.pre_annotation_tool_config import (
    PreAnnotateCVATConfig,
)
from mlcvzoo_base.tools.logger import Logger
from mlcvzoo_base.utils import draw_on_image, generate_detector_colors
from mlcvzoo_base.utils.file_utils import get_basename, get_file_list
from mlcvzoo_base.utils.image_io_utils import VideoLiveOutput

logger = logging.getLogger(__name__)


class PreAnnotationTool(ConfigBuilder):
    """
    Tool that generates predictions and uploads these to CVAT as initialization for new tasks
    """

    argparse_description: str = (
        "Generate predictions and upload these to "
        "CVAT as initialization for new tasks"
    )

    def __init__(
        self,
        yaml_config_path: Optional[str] = None,
        configuration: Optional[PreAnnotateCVATConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        no_checks: bool = False,
    ):
        """
        Instantiates a PreAnnotationTool object

        Args:
            yaml_config_path: (Optional) A yaml filepath where to build the configuration
                               object from
            configuration: (Optional) An already existing configuration object
            string_replacement_map: A dictionary that defines placeholders which can be used
                                    while parsing the file. They can be understood as variables
                                    that can be used to define configs that are valid across
                                    multiple devices.
            no_checks: Whether the configuration object should be checked for mutual exclusiveness
                       and the "check_values" method for each attribute of the supertype
                       "BaseConfigClass" should be called
        """

        try:
            ConfigBuilder.__init__(
                self,
                class_type=PreAnnotateCVATConfig,
                configuration=configuration,
                yaml_config_path=yaml_config_path,
                argparse_module_description=PreAnnotationTool.argparse_description,
                string_replacement_map=string_replacement_map,
                no_checks=no_checks,
                use_argparse_fallback=True,
            )

            self.configuration: PreAnnotateCVATConfig = cast(  # type: ignore
                PreAnnotateCVATConfig,
                self.configuration,
            )
        except ValueError as value_error:
            handle_value_error_for_tool_configuration(
                value_error=value_error, config_builder_instance=self
            )
            raise value_error

        self.video_live_output: Optional[VideoLiveOutput] = None

        self.model_registry = ModelRegistry()

    @staticmethod
    def setup_argparse() -> argparse.ArgumentParser:
        """
        Returns:
            An ArgumentParser instance that handles the commandline parameters of
            the PreAnnotationTool
        """

        return ConfigBuilder._setup_argparse(
            argparse_module_description=PreAnnotationTool.argparse_description,
            add_argparse_parameters=PreAnnotationTool._add_argparse_parameters,
        )

    def __create_object_detection_model(self) -> ObjectDetectionModel:  # type: ignore
        object_detection_model: Model[PredictionType, ConfigurationType, DataType]  # type: ignore
        object_detection_model = self.model_registry.init_model(
            model_config=self.configuration.model_config,
            string_replacement_map=self.configuration.string_replacement_map,
        )

        if not isinstance(object_detection_model, ObjectDetectionModel):
            raise ValueError(
                "This evaluation can only be used with models that "
                "inherit from 'mlcvzoo.api.model.ObjectDetectionModel'"
            )

        return object_detection_model

    def __gather_image_paths(self) -> List[str]:

        image_paths: List[str] = []

        disk_image_file_map: Dict[str, str] = {}

        input_image_types = self.configuration.input_image_type.split("|")

        input_image_paths: List[str] = []
        for input_image_type in input_image_types:
            input_image_paths.extend(
                get_file_list(
                    input_dir=self.configuration.root_image_dir,
                    search_subfolders=True,
                    file_extension=self.configuration.input_image_type,
                )
            )

        for image_path in input_image_paths:
            disk_image_file_map[get_basename(image_path)] = image_path

        for (
            dump_task_config
        ) in self.configuration.cvat_annotation_handler_config.dump_task_configs:
            source_zip_file = zipfile.ZipFile(dump_task_config.target_zip_path)

            logger.debug("Get image paths from '%s'" % dump_task_config.target_zip_path)

            task_image_paths = (
                source_zip_file.read("ImageSets/Main/default.txt")
                .decode("utf-8")
                .split("\n")
            )

            for task_image_path in task_image_paths:
                task_image_basename = get_basename(task_image_path)
                if task_image_basename in disk_image_file_map:
                    image_paths.append(disk_image_file_map[task_image_basename])

        logger.debug("Gathered '%s' image paths for prediction." % len(image_paths))

        return image_paths

    def generate_annotations(self) -> None:
        """
        Generate PASCAL-VOC annotations using the configured model and
        store these annotations at the configured location

        Returns:
            None
        """

        object_detection_model: ObjectDetectionModel = (  # type: ignore
            self.__create_object_detection_model()
        )

        image_paths: List[str] = self.__gather_image_paths()

        process_bar = tqdm(image_paths, desc="Generate predictions")

        if self.configuration.show_predictions:
            self.video_live_output = VideoLiveOutput(mode=VideoLiveOutput.MODE_STEP)

        rgb_colors: List[Tuple[int, int, int]] = []
        if self.video_live_output is not None:
            rgb_colors = generate_detector_colors(
                num_classes=object_detection_model.num_classes
                if isinstance(object_detection_model.num_classes, int)
                else object_detection_model.num_classes()  # type: ignore
            )

        for image_path in process_bar:

            if (
                self.video_live_output is not None
                and self.video_live_output.is_terminated()
            ):
                break

            image = cv2.imread(image_path)

            predicted_annotation: BaseAnnotation = BaseAnnotation(
                image_path=image_path,
                annotation_path=os.path.join(
                    self.configuration.output_xml_dir, f"{get_basename(image_path)}.xml"
                ),
                image_shape=(image.shape[0], image.shape[1]),
                image_dir="",
                replacement_string="",
                annotation_dir=self.configuration.output_xml_dir,
                classifications=[],
                bounding_boxes=[],
                segmentations=[],
            )

            if not os.path.isfile(predicted_annotation.annotation_path) or (
                os.path.isfile(predicted_annotation.annotation_path)
                and self.configuration.overwrite_existing_annotations
            ):

                # TODO: When ReadFromFile model is supporting images, then switch
                #       to predict on image and not image-path
                _, predicted_bounding_boxes = object_detection_model.predict(
                    data_item=image_path
                )

                logger.info("Predicted bounding boxes: %s" % predicted_bounding_boxes)

                if self.video_live_output is not None:
                    self.video_live_output.output_frame(
                        draw_on_image(
                            frame=image,
                            rgb_colors=rgb_colors,
                            bounding_boxes=predicted_bounding_boxes,
                            thickness=5,
                        )
                    )

                predicted_annotation.bounding_boxes = predicted_bounding_boxes

                annotation_to_xml(
                    annotation=predicted_annotation,
                )

    def run(self) -> None:
        """
        Generate and upload the annotations to the CVAT instance

        1. Download all task information
        2. Parse the image-paths utilizing the information of the downloaded
           tasks
        3. Run the model based on the gathered image paths and generate the
           respective annotation files
        4. Uploaded the annotations to CVAT

        Returns:
            None
        """

        cvat_annotation_handler_instance = CVATAnnotationHandler(
            configuration=self.configuration.cvat_annotation_handler_config
        )

        cvat_annotation_handler_instance.download_all_tasks()

        if self.configuration.generate_annotations:
            self.generate_annotations()

        cvat_annotation_handler_instance.upload_all_tasks()


def main() -> None:
    """
    Main entry point of the PreAnnotationTool

    Returns:
        None
    """

    args = PreAnnotationTool.setup_argparse().parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="PreAnnotationTool",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    try:
        pre_annotation_tool = PreAnnotationTool()
        pre_annotation_tool.run()
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
