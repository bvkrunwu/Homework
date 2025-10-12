import os

import pytest

from src.decorators import log


@pytest.fixture(autouse=True)
def cleanup_log_file():
    yield
    for filename in ["test_log.txt"]:
        if os.path.exists(filename):
            os.remove(filename)


def test_successful_execution(capsys):
    @log()
    def successful_func():
        return True

    successful_func()
    captured = capsys.readouterr()
    assert captured.out.strip() == "successful_func ok"


def test_error_in_console(capsys):
    @log()
    def failing_func():
        raise ValueError("Test Error")

    with pytest.raises(ValueError):
        failing_func()

    captured = capsys.readouterr()
    expected_output = "failing_func error: ValueError. Inputs: (), {}"
    assert captured.out.strip() == expected_output


def test_write_to_file(tmp_path):
    temp_filename = tmp_path / "test_log.txt"

    @log(str(temp_filename))
    def another_success():
        pass

    another_success()
    with open(temp_filename, "r") as f:
        content = f.read().strip()
        assert content == "another_success ok"


def test_file_logging_on_failure(tmp_path):
    temp_filename = tmp_path / "failure_log.txt"

    @log(str(temp_filename))
    def fail():
        raise TypeError("Type mismatch!")

    with pytest.raises(TypeError):
        fail()

    with open(temp_filename, "r") as f:
        content = f.read().strip()
        expected_output = "fail error: TypeError. Inputs: (), {}"
        assert content == expected_output
