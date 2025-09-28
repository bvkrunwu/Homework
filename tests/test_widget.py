from typing import Tuple

import pytest
from pytest import FixtureRequest

from src.widget import mask_account_card


# Фикстуры с кортежами
@pytest.fixture
def minimal_card_data() -> Tuple[str, str]:
    """Минимальная длина номера карты (16 цифр)."""
    return "Visa 4149371632766405", "Visa 4149 37** **** 6405"


@pytest.fixture
def maximal_account_data() -> Tuple[str, str]:
    """Максимальная длина номера счета (20 символов)."""
    return "Счет 40817810800000000001", "Счет **0001"


# Фикстуры с параметризацией
@pytest.fixture(params=["", "SingleWord", "Three Words Here", "Invalid*Symbol"])
def invalid_input_data(request: FixtureRequest) -> str:
    """Некорректные входные данные."""
    return request.param  # type: ignore


# Тестовые функции
def test_minimal_card_length(minimal_card_data: Tuple[str, str]) -> None:
    input_str, expected = minimal_card_data
    assert mask_account_card(input_str) == expected


def test_maximal_account_length(maximal_account_data: Tuple[str, str]) -> None:
    input_str, expected = maximal_account_data
    assert mask_account_card(input_str) == expected
