import logging
import colorlog
from src.utils.constants import LOG_PATH, LOG_CLEAR


def init_logger(*, dunder_name: str, testing_mode: bool) -> logging.Logger:
    log_format = (
        "%(asctime)s - "
        "%(name)s - "
        "%(funcName)s - "
        "%(levelname)s - "
        "%(message)s"
    )
    """ Initialize logging """

    bold_seq = "\033[1m"
    colorlog_format = f"{bold_seq} " "%(log_color)s " f"{log_format}"
    colorlog.basicConfig(format=colorlog_format)
    logger = logging.getLogger(dunder_name)

    if testing_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if LOG_CLEAR == "True":
        mode = "w"
    elif LOG_CLEAR == "False":
        mode = "a"
    else:
        raise ValueError("LOG_CLEAR must be True or False")

    fh = logging.FileHandler(
        filename=f"{LOG_PATH}/app.log", mode=mode, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    fh = logging.FileHandler(
        filename=f"{LOG_PATH}/app.warning.log", mode=mode, encoding="utf-8")
    fh.setLevel(logging.WARNING)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    fh = logging.FileHandler(
        filename=f"{LOG_PATH}/app.error.log", mode=mode, encoding="utf-8")
    fh.setLevel(logging.ERROR)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
