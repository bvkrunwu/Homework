import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.fixture(scope="module")
def valid_card_numbers():
    """Возвращает список валидных номеров банковских карт."""
    return ["1234567890123456", "9876543210987654", "1111222233334444"]


@pytest.fixture(scope="module")
def valid_account_numbers():
    """Возвращает список валидных номеров банковских счетов."""
    return ["1234567890123456", "9876543210987654"]


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number_success(input_data, expected_output):
    result = get_mask_card_number(input_data)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output", [("1234567890123456", "**3456"), ("9876543210987654", "**7654")]
)
def test_get_mask_account_success(input_data, expected_output):
    result = get_mask_account(input_data)
    assert result == expected_output


def test_empty_list_input():
    with pytest.raises(AttributeError):
        get_mask_card_number([])
    with pytest.raises(AttributeError):
        get_mask_account([])


def test_get_mask_card_number_empty_string():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Ошибка: пустой номер карты."


def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123456789012345")
    assert str(exc_info.value) == "Ошибка: неверная длина номера карты."


def test_get_mask_card_number_non_digit_chars():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("12345678901234A6")
    assert str(exc_info.value) == "Ошибка: неверный формат номера карты."


def test_get_mask_account_empty_string():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Ошибка: пустой номер счета."


def test_get_mask_account_too_short():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("123")
    assert str(exc_info.value) == "Ошибка: недостаточная длина номера счета."


def test_get_mask_account_non_digit_chars():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("1234ABCD")
    assert str(exc_info.value) == "Ошибка: неверный формат номера счета."