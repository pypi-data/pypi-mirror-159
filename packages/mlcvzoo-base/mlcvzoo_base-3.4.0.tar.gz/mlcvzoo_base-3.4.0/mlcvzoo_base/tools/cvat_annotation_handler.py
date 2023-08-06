# Copyright 2022 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

import logging
import sys

from mlcvzoo_base.data_preparation.cvat_annotation_handler.cvat_annotation_handler import (
    CVATAnnotationHandler,
)
from mlcvzoo_base.tools.logger import Logger

logger = logging.getLogger(__name__)


def main() -> None:
    """
    Main entry point of the CVATAnnotationHandler tool

    Returns:
        None
    """

    args = CVATAnnotationHandler.setup_argparse().parse_args()

    Logger.init_logging_basic(
        log_dir=args.log_dir,
        log_file_postfix="CVATAnnotationHandler",
        no_stdout=False,
        root_log_level=args.log_level,
    )

    try:
        cvat_annotation_handler = CVATAnnotationHandler()
        cvat_annotation_handler.run()
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
