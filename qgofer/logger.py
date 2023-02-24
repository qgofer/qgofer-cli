"""Logging module for qgofer."""
import datetime
import logging
import sys

from .utils import generate_uuid, get_log_path


def get_logger(log_path=None, run_id=None):
    """Returns a generic logger for logging relevant information pertaining to run of qgofer.

    Returns:
        Python logger object
    """
    log_path = get_log_path(log_path)
    # create logger with 'spam_application'
    logger = logging.getLogger("ce_application")
    logger.setLevel(logging.DEBUG)

    if not run_id:
        run_id = generate_uuid()

    file_path = f"{log_path}/{run_id}_log_{datetime.datetime.now().strftime('%y_%m_%d_%H_%M_%S')}.log"
    if not logger.handlers:
        # create file handler which logs even debug messages
        fh = logging.FileHandler(file_path)
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler(stream=sys.stdout)
        ch.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.file_path = file_path

    return logger
