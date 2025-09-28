from typing import Any
from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture(scope="module")
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с набором транзакций для тестирования."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03"},
        {"id": 4, "state": "PENDING", "date": "2023-01-04"},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-05"},
    ]


@pytest.mark.parametrize(
    "state,expected_ids",
    [
        ("EXECUTED", [1, 3, 5]),
        ("APPROVED", []),
    ],
)
def test_filter_by_state(sample_transactions: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    """Тестирование фильтрации транзакций по состоянию."""
    result = filter_by_state(sample_transactions, state)
    actual_ids = [t["id"] for t in result]
    assert actual_ids == expected_ids


@pytest.mark.parametrize(
    "descending,expected_order",
    [
        (True, [5, 4, 3, 2, 1]),
        (False, [1, 2, 3, 4, 5]),
    ],
)
def test_sort_by_date(sample_transactions: List[Dict[str, Any]], descending: bool, expected_order: List[int]) -> None:
    """Тестирование сортировки транзакций по дате."""
    result = sort_by_date(sample_transactions, descending)
    actual_order = [t["id"] for t in result]
    assert actual_order == expected_order
