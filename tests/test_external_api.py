from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_transaction_amount_to_rubles


@pytest.fixture
def sample_transaction_usd():
    """Образец транзакции в долларах."""
    return {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}


@pytest.fixture
def sample_transaction_eur():
    """Образец транзакции в евро."""
    return {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}


@pytest.fixture
def sample_transaction_other():
    """Образец транзакции в другой валюте."""
    return {"operationAmount": {"amount": "100", "currency": {"code": "GBP"}}}


def test_convert_transaction_amount_to_rubles_usd(sample_transaction_usd):
    """Тест конвертации долларовой транзакции в рубли."""
    mock_response = Mock(status_code=200)
    mock_response.json.return_value = {"result": 7500}

    with patch("requests.get", return_value=mock_response):
        result = convert_transaction_amount_to_rubles(sample_transaction_usd)

    assert result == 7500


def test_convert_transaction_amount_to_rubles_eur(sample_transaction_eur):
    """Тест конвертации в евро транзакции в рубли."""
    mock_response = Mock(status_code=200)
    mock_response.json.return_value = {"result": 8500}

    with patch("requests.get", return_value=mock_response):
        result = convert_transaction_amount_to_rubles(sample_transaction_eur)

    assert result == 8500


def test_convert_transaction_amount_to_rubles_other_currency(sample_transaction_other):
    """Тест возвращения исходной суммы для неподдерживаемой валюты."""
    result = convert_transaction_amount_to_rubles(sample_transaction_other)
    assert result == 100.0


def test_convert_transaction_amount_to_rubles_http_error(sample_transaction_usd):
    """Тест обработки HTTP ошибки."""
    mock_response = Mock(status_code=400)
    mock_response.raise_for_status.side_effect = Exception("Bad Request")

    with patch("requests.get", return_value=mock_response):
        result = convert_transaction_amount_to_rubles(sample_transaction_usd)

    assert result is None


def test_convert_transaction_amount_to_rubles_general_error(sample_transaction_usd):
    """Тест обработки общей ошибки."""
    with patch("requests.get", side_effect=Exception("Network Error")):
        result = convert_transaction_amount_to_rubles(sample_transaction_usd)

    assert result is None
