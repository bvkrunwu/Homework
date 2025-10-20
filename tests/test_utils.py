import json
from unittest.mock import Mock, patch

from src.utils import load_transactions

VALID_DATA = [{"transaction_id": 1, "amount": 100}, {"transaction_id": 2, "amount": 200}]


def test_missing_file():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        result = load_transactions("missing/file.json")
        assert isinstance(result, list)
        assert not result


def test_invalid_json():
    mock_file = Mock()
    mock_file.read.return_value = "{invalid}"

    with (
        patch("builtins.open", return_value=mock_file),
        patch("src.utils.json.load", side_effect=json.JSONDecodeError("", "", 0)),
    ):
        result = load_transactions("invalid/json/file.json")
        assert isinstance(result, list)
        assert not result


def test_non_list_data():
    mock_file = Mock()
    mock_file.read.return_value = "{}"

    with (
        patch("builtins.open", return_value=mock_file),
        patch("src.utils.json.load", return_value={"not_a_list": True}),
    ):
        result = load_transactions("non/list/data.json")
        assert isinstance(result, list)
        assert not result


def test_unexpected_exception_handling():
    with patch("builtins.open", side_effect=Exception("Unexpected error")):
        result = load_transactions("unexpected/error/file.json")
        assert isinstance(result, list)
        assert not result
