import os
from unittest import mock
import logging
import pytest
import src.utils.logger as logger


def test_leve_debugl():
    testing_mode = True
    assert logger.level(testing_mode) == logging.DEBUG


def test_level_info():
    testing_mode = False
    assert logger.level(testing_mode) == logging.INFO


@mock.patch.dict(os.environ, {"LOG_CLEAR": "True"})
def test_log_write_mode_w():
    log_clear = os.getenv("LOG_CLEAR")
    assert logger.log_write_mode(str(log_clear)) == "w"


@mock.patch.dict(os.environ, {"LOG_CLEAR": "False"})
def test_log_write_mode_a():
    log_clear = os.getenv("LOG_CLEAR")
    assert logger.log_write_mode(str(log_clear)) == "a"


@mock.patch.dict(os.environ, {"LOG_CLEAR": ""})
def test_log_write_mode_invalid():
    log_clear = os.getenv("LOG_CLEAR")
    with pytest.raises(ValueError):
        logger.log_write_mode(str(log_clear))
