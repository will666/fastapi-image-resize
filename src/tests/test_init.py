import pytest
import os
from unittest import mock
from src.utils.constants import LOG_LEVEL
import src.utils.init as init
import string
import random

rs = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))


@mock.patch.dict(os.environ, {"LOG_PATH": "logs"})
def test_log_path_valid() -> None:
    log_path = os.getenv("LOG_PATH")
    assert init.log_path(str(log_path)) == "logs"


@mock.patch.dict(os.environ, {"LOG_PATH": ""})
def test_log_path_invalid() -> None:
    with pytest.raises(ValueError):
        log_path = os.getenv("LOG_PATH")
        init.log_path(str(log_path))


def test_need_create_log_path():
    assert init.create_log_path(f"/tmp/{rs}") is True


def test_no_need_create_log_path():
    assert init.create_log_path(f"/tmp/{rs}") is False


@mock.patch.dict(os.environ, {"LOG_LEVEL": "DEBUG"})
def test_log_level_valid() -> None:
    assert LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]


@mock.patch.dict(os.environ, {"LOG_LEVEL": "TEST"})
def test_log_level_invalid() -> None:
    with pytest.raises(ValueError):
        log_level = os.getenv("LOG_LEVEL")
        init.testing_mode(str(log_level))


@mock.patch.dict(os.environ, {"LOG_LEVEL": "DEBUG"})
def test_testing_mode_true() -> None:
    log_level = os.getenv("LOG_LEVEL")
    assert init.testing_mode(str(log_level))


@mock.patch.dict(os.environ, {"LOG_LEVEL": "INFO"})
def test_testing_mode_false() -> None:
    log_level = os.getenv("LOG_LEVEL")
    assert not init.testing_mode(str(log_level))
