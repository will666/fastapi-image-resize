import pytest
from pytest import MonkeyPatch
import os
from src.utils.constants import LOG_PATH, LOG_LEVEL
import src.utils.init as init


def test_log_path(monkeypatch: MonkeyPatch):
    assert os.path.exists(LOG_PATH)
    assert os.path.isdir(LOG_PATH)
    assert os.path.exists(f"{LOG_PATH}/app.log")
    assert os.path.exists(f"{LOG_PATH}/app.warning.log")
    assert os.path.exists(f"{LOG_PATH}/app.error.log")

    # monkeypatch.setenv('LOG_PATH', '')
    # with pytest.raises(ValueError):
    #     init.logger


# @pytest.mark.run('last')
def test_testing_mode() -> None:
    assert LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]
    if LOG_LEVEL == "DEBUG":
        assert init.testing_mode is True
    if LOG_LEVEL in ["INFO", "WARNING", "ERROR"]:
        assert init.testing_mode is False
    # else:
    #     raise ValueError("LOG_LEVEL must be DEBUG, INFO, WARNING, or ERROR")
