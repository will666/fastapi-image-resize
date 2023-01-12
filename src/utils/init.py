import os
from src.utils.logger import init_logger
from src.utils.constants import (
    LOG_PATH,
    LOG_LEVEL,
)


if LOG_PATH == None:
    raise ValueError("LOG_PATH must be a valid path")
elif not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
else:
    pass

testing_mode = bool

if LOG_LEVEL == "DEBUG":
    testing_mode = True
elif LOG_LEVEL in ["INFO", "WARNING", "ERROR"]:
    testing_mode = False
else:
    raise ValueError("LOG_LEVEL must be DEBUG, INFO, WARNING, or ERROR")

logger = init_logger(dunder_name=__name__, testing_mode=testing_mode)
