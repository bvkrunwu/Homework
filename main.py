from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import read_csv_transactions, read_excel_transactions
from src.utils import load_transactions
from src.widget import get_date


def main():
    """
    Основная функция программы, управляющая логикой взаимодействия с пользователем и связывающая все модули.
    """
    # Приветствие пользователя
    print(
        """
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    )

    # Выбор формата файла
    choice = input("\nВаш выбор: ").strip()

    # Загрузка транзакций в зависимости от выбора пользователя
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = load_transactions("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv_transactions("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_excel_transactions("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор пункта меню!")
        return

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = (
            input(
                "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\nВаш выбор: "
            )
            .strip()
            .upper()
        )

        if status in valid_statuses:
            break

        print(f"\nСтатус операции '{status}' недоступен.")

    print(f'\nОперации отфильтрованы по статусу "{status}"')
    transactions = list(filter_by_state(transactions, status))

    # Дополнительные опции фильтрации и сортировки
    sort_choice = input("\nОтсортировать операции по дате? Да/Нет ").strip().lower()
    if sort_choice.startswith(("y", "д")):
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        ascending = order.startswith(("v", "п"))
        transactions = sort_by_date(transactions, ascending)

    ruble_choice = input("\nВыводить только рублевые транзакции? Да/Нет ").strip().lower()
    if ruble_choice.startswith(("y", "д")):
        transactions = list(filter_by_currency(transactions, "RUB"))

    word_choice = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет ").strip().lower()
    if word_choice.startswith(("y", "д")):
        search_word = input("Введите искомое слово: ").strip()
        transactions = list(filter(lambda t: search_word in t["description"], transactions))

    # Вывод итогового списка транзакций
    print("\nРаспечатываю итоговый список транзакций...\n")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    for idx, transaction in enumerate(transactions, 1):
        from_info = transaction.get("from", "")
        to_info = transaction.get("to", "")

        # Маска для номера карты/счета отправителя
        from_masked = None
        if from_info:
            parts = str(from_info).split()
            if len(parts) >= 2:
                label, number = parts[-2:]
                if label.lower().startswith("счет"):
                    from_masked = get_mask_account(number)
                else:
                    from_masked = get_mask_card_number(number)
            else:
                from_masked = from_info

        # Маска для номера карты/счета получателя
        to_masked = None
        if to_info:
            parts = str(to_info).split()
            if len(parts) >= 2:
                label, number = parts[-2:]
                if label.lower().startswith("счет"):
                    to_masked = get_mask_account(number)
                else:
                    to_masked = get_mask_card_number(number)
            else:
                to_masked = to_info

        # Форматирование даты
        date_formatted = get_date(transaction["date"])

        # Получение суммы и валюты (адаптировано для разных форматов данных)
        if isinstance(transaction.get("operationAmount"), dict):
            # Обработка JSON структуры
            amount = transaction.get("operationAmount", {}).get("amount", "N/A")
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "N/A")
        else:
            # Обработка CSV/XLSX структуры
            amount = transaction.get("amount", "N/A")
            currency = transaction.get("currency_name", "N/A")

        # Вывод информации о транзакции
        print(f"{idx}. {date_formatted} {transaction['description']}")
        if from_masked is not None:
            print(f"{from_masked} -> ", end="")
        print(f"{to_masked or ''}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
