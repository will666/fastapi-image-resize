import os
from src.utils.logger import init_logger
from src.utils.constants import (
    LOG_PATH,
    LOG_LEVEL,
)


def log_path(log_path: str = LOG_PATH) -> str:
    if log_path == "":
        raise ValueError("LOG_PATH must be a valid path")
    return str(log_path)


def create_log_path(log_path: str = log_path()) -> bool:
    if not os.path.exists(log_path):
        os.mkdir(log_path)
        return True
    return False


def testing_mode(log_level: str) -> bool:
    if log_level == "DEBUG":
        return True
    elif log_level in ["INFO", "WARNING", "ERROR"]:
        return False
    else:
        raise ValueError("LOG_LEVEL must be DEBUG, INFO, WARNING, or ERROR")


create_log_path()
logger = init_logger(
    dunder_name=__name__, testing_mode=testing_mode(LOG_LEVEL)
)
