import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture(scope="module")
def sample_transactions():
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
        ("EXECUTED", [1, 3, 5]),  # Нормальное выполнение
        ("APPROVED", []),  # Нет транзакций с таким статусом
    ],
)
def test_filter_by_state(sample_transactions, state, expected_ids):
    """Тестирование фильтрации транзакций по состоянию."""
    result = filter_by_state(sample_transactions, state)
    actual_ids = [t["id"] for t in result]
    assert actual_ids == expected_ids


@pytest.mark.parametrize(
    "descending,expected_order",
    [
        (True, [5, 4, 3, 2, 1]),  # Сортировка по убыванию
        (False, [1, 2, 3, 4, 5]),  # Сортировка по возрастанию
    ],
)
def test_sort_by_date(sample_transactions, descending, expected_order):
    """Тестирование сортировки транзакций по дате."""
    result = sort_by_date(sample_transactions, descending)
    actual_order = [t["id"] for t in result]
    assert actual_order == expected_order