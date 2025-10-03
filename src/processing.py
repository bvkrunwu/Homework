def filter_by_state(
    transactions_list: list[dict[str, str | int]], state: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """
    Фильтрация списка транзакций по указанному состоянию.

    Args:
    transactions_list (list): Список словарей, каждый из которых представляет отдельную транзакцию.
    state (str): Строка, определяющая статус транзакции для фильтрации (по умолчанию 'EXECUTED').

    Returns:
    list: Новый список, содержащий только транзакции с соответствующим статусом.
    """
    # Создание нового списка, содержащего только транзакции с нужным состоянием
    filtered_transactions = [
        transaction  # Сохраняется каждая транзакция...
        for transaction in transactions_list  # перебираются все транзакции из исходного списка...
        if transaction.get("state") == state  # если её состояние равно переданному аргументу state
    ]
    # Возврат полученного списка отфильтрованных транзакций
    return filtered_transactions


def sort_by_date(transactions_list: list[dict[str, str | int]], descending: bool = True) -> list[dict[str, str | int]]:
    """
    Сортирует список транзакций по дате проведения.

    Args:
    transactions_list (list): Список словарей, содержащих данные о транзакциях.
    descending (bool): Параметр, определяющий порядок сортировки (True - по убыванию, False - по возрастанию).
                       По умолчанию установлен True (сортируем по убыванию дат).

    Returns:
    list: Отсортированная копия исходного списка транзакций.
    """
    # Создаем новую отсортированную копию списка транзакций
    sorted_transactions = sorted(
        transactions_list,  # Исходный список транзакций
        key=lambda x: x["date"],  # Ключевое поле для сортировки - дата транзакции
        reverse=descending,  # Направление сортировки (по убыванию, если True)
    )
    # Возвращаем полученный отсортированный список
    return sorted_transactions
