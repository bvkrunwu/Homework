import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.fixture
def minimal_card_data():
    """Минимальная длина номера карты (16 цифр)."""
    return "Visa 4149371632766405", "Visa 4149 37** **** 6405"


@pytest.fixture
def maximal_account_data():
    """Максимальная длина номера счета (20 символов)."""
    return "Счет 40817810800000000001", "Счет **0001"


@pytest.fixture(params=["", "SingleWord", "Three Words Here", "Invalid*Symbol"])
def invalid_input_data(request):
    """Расширенный набор некорректных входных данных."""
    return request.param


@pytest.fixture
def valid_iso_date():
    """Корректная ISO-дата."""
    return "2023-10-05T14:30:00.123456", "05.10.2023"


@pytest.fixture(params=["", "2023-02-30T00:00:00.000000"])
def invalid_iso_dates(request):
    """Некорректные ISO-даты."""
    return request.param


def test_minimal_card_length(minimal_card_data):
    """Тестирование минимальной длины номера карты (16 цифр)."""
    input_string, expected_output = minimal_card_data
    result = mask_account_card(input_string)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


def test_maximal_account_length(maximal_account_data):
    """Тестирование максимальной длины номера счета (20 символов)."""
    input_string, expected_output = maximal_account_data
    result = mask_account_card(input_string)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


@pytest.mark.parametrize("input_data", ["", "SingleWord", "Three Words Here", "Invalid*Symbol"])
def test_invalid_inputs(input_data):
    """Тестирование реакции на неверные входные данные."""
    with pytest.raises(ValueError):
        mask_account_card(input_data)


def test_incorrect_parts_count():
    """Тестирование реакции на неправильное количество частей в строке."""
    with pytest.raises(ValueError):
        mask_account_card("Invalid Input Format")


def test_valid_iso_date(valid_iso_date):
    """Тестирование корректного преобразования ISO-даты."""
    iso_date, expected_output = valid_iso_date
    result = get_date(iso_date)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


def test_invalid_iso_dates(invalid_iso_dates):
    """Тестирование реакции на некорректные ISO-даты."""
    with pytest.raises(ValueError):
        get_date(invalid_iso_dates)


def test_missing_date():
    """Тестирование реакции на пустую строку."""
    with pytest.raises(ValueError):
        get_date("")