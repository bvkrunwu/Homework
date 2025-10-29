import pytest

from src.bank_operations import process_bank_operations, process_bank_search


# Фикстура с общими банковскими данными
@pytest.fixture(scope="module")
def bank_data():
    """Фикстура с примером банковских данных"""
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


# ⬇️ Тесты для функции process_bank_search ⬇️


@pytest.mark.parametrize(
    "search_term, expected_count",
    [
        ("организации", 1),
        ("неверный_поиск", 0),
    ],
)
def test_process_bank_search(bank_data, search_term, expected_count):
    result = process_bank_search(bank_data, search_term)
    assert len(result) == expected_count, f"Ошибка при поиске '{search_term}'"


def test_process_bank_search_empty_input(bank_data):
    with pytest.raises(ValueError):
        process_bank_search(None, "любое слово")


# ⬇️ Тесты для функции process_bank_operations ⬇️


@pytest.mark.parametrize(
    "categories, expected_result",
    [(["Перевод организации"], {"Перевод организации": 1}), (["Неверная категория"], {}), ([], {})],
)
def test_process_bank_operations(bank_data, categories, expected_result):
    result = process_bank_operations(bank_data, categories)
    assert result == expected_result, f"Ошибка при категоризации: {categories}"


def test_process_bank_operations_invalid_type():
    with pytest.raises(ValueError):
        process_bank_operations(None, [])
