import os
from dotenv import load_dotenv

ROOT_DIR = os.path.abspath("src")

load_dotenv(dotenv_path=f"{ROOT_DIR}/../.env", override=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_PATH = os.getenv(f"{ROOT_DIR}/LOG_PATH", "logs")
LOG_CLEAR = os.getenv("LOG_CLEAR", "False").capitalize()
LOG_DISPLAY_ENV_VARS = os.getenv("LOG_DISPLAY_ENV_VARS", "False").capitalize()
