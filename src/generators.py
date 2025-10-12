from typing import Any, Dict, Generator, Iterable, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterable[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданному коду валюты.
    Функция получает список транзакций, затем выбирает только те транзакции,
    в которых валюта совпадает либо по коду, либо по имени.

    Args:
    transactions (list[dict]): Список словарей, содержащих информацию о транзакциях.
    currency_code (str): Строка, содержащая код валюты для фильтрации (например, "USD").

    Returns:
    Iterable[dict]: Итератор, выдающий транзакции, соответствующие заданной валюте.
    """

    # Фильтрация транзакций, имеющих ключ 'operationAmount'.
    operations_amount = filter(lambda t: "operationAmount" in t, transactions)

    # Выбор транзакций, содержащих информацию о валюте ('currency')
    currency_info = filter(lambda t: "currency" in t["operationAmount"], operations_amount)

    # Поиск транзакций, где код или название валюты совпадают с искомым значением.
    matching_currency = filter(
        lambda t: (
            t["operationAmount"]["currency"].get("code") == currency_code
            or t["operationAmount"]["currency"].get("name") == currency_code
        ),
        currency_info,
    )

    return matching_currency


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Принимает список словарей с транзакциями
     и возвращающая описание каждой операции по очереди.
    Функция-генератор последовательно проходит по списку транзакций и возвращает строки с описаниями операций.
    Ожидается, что каждая транзакция представлена в виде словаря, содержащего ключ 'description',
    который хранит текстовую информацию о самой транзакции.

    Args:
    transactions (list of dicts): Список словарей, содержащих данные о транзакциях.

    Yields:
    Генератор, выдающий строку с описанием транзакции при каждом обращении.
    """

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.
    Функция-генератор создает последовательность номеров банковских карт в формате XXXX XXXX XXXX XXXX,
    начиная с указанного стартового числа и заканчивая финишным числом включительно.
    Каждый номер дополняется ведущими нулями до общей длины 16 символов.

    Args:
        start (int): Начальное значение диапазона (включительно)
        stop (int): Конечное значение диапазона (включительно)

    Raises:
        TypeError: Если хотя бы один из аргументов не является целым числом.
        ValueError: Если начальное значение меньше единицы, конечное значение превышает максимальное,
                    или начальное значение больше конечного.

    Yields:
        str: Номер банковской карты в формате XXXX XXXX XXXX XXXX
    """

    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("start и stop должны быть целыми числами")
    if start <= 0 or stop > 9999999999999999:
        raise ValueError("Диапазон должен быть от 1 до 9999999999999999")
    if start > stop:
        raise ValueError("Начальное значение должно быть меньше или равно конечному значению")

    for number in range(start, stop + 1):
        formatted_numbers = f"{number:016d}"
        yield f"{formatted_numbers[:4]} {formatted_numbers[4:8]} {formatted_numbers[8:12]} {formatted_numbers[12:]}"
