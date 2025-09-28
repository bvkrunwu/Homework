import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.fixture(scope="module")
def valid_card_numbers() -> list[str]:
    """Возвращает список валидных номеров банковских карт"""
    return ["1234567890123456", "9876543210987654", "1111222233334444"]


@pytest.fixture(scope="module")
def valid_account_numbers() -> list[str]:
    """Возвращает список валидных номеров банковских счетов"""
    return ["12345678901234567890", "98765432109876543210"]


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number_success(input_data: str, expected_output: str) -> None:
    result = get_mask_card_number(input_data)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("12345678901234567890", "**7890"),
        ("98765432109876543210", "**3210"),
    ],
)
def test_get_mask_account_success(input_data: str, expected_output: str) -> None:
    result = get_mask_account(input_data)
    assert result == expected_output


# Остальные тесты остаются аналогичными с добавлением аннотаций типов
