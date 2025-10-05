def filter_by_currency(transactions, currency_code):
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


def transaction_descriptions(transactions):
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
