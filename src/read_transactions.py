from pathlib import Path
from typing import Any, Dict, List, Optional, cast

import pandas as pd


def read_csv_transactions(file_path_csv: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Читает транзакции из CSV-файла и конвертирует их в список словарей.

    Args:
        file_path_csv (Optional[str]): Путь к CSV-файлу с транзакциями. По умолчанию None.

            Если путь не передан, используется стандартный путь:
                `<корень_проекта>/data/transactions.csv`

    Returns:
        List[Dict[str, Any]]: Список словарей, где каждый словарь соответствует строке из CSV-файла.
                              Каждый ключ словаря соответствует названию столбца.

        В случае возникновения ошибки возвращается пустой список.
    """

    # Проверяем наличие переданного пути к файлу
    if not file_path_csv:
        # Определяем корень проекта относительно расположения текущего файла (__file__)
        project_root = Path(__file__).resolve().parent.parent
        # Формируем полный путь к файлу операций в каталоге 'data'
        file_path_csv = str(project_root / "data" / "transactions.csv")

    try:
        # Читаем CSV-файл
        df = pd.read_csv(file_path_csv, sep=";", encoding="utf-8")

        # Преобразуем DataFrame в список словарей, где каждый словарь соответствует записи
        return cast(List[Dict[str, Any]], df.to_dict("records"))

    except Exception as e:
        # Обрабатываем любые возникшие ошибки и выводим информативное сообщение
        print(f"Произошла ошибка при обработке CSV-файла: {e}")

        return []


def read_excel_transactions(file_path_excel: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Читает транзакции из Excel-файла и конвертирует их в список словарей.

    Args:
        file_path_excel (Optional[str]): Путь к Excel-файлу с транзакциями. По умолчанию None.

            Если путь не передан, используется стандартный путь:
                `<корень_проекта>/data/transactions_excel.xlsx`

    Returns:
        List[Dict[str, Any]]: Список словарей, где каждый словарь соответствует строке из Excel-файла.
                              Каждый ключ словаря соответствует названию столбца.

        В случае возникновения ошибки возвращается пустой список.
    """

    # Проверяем наличие переданного пути к файлу
    if not file_path_excel:
        # Определяем корень проекта относительно расположения текущего файла (__file__)
        project_root = Path(__file__).resolve().parent.parent
        # Формируем полный путь к файлу операций в каталоге 'data'
        file_path_excel = str(project_root / "data" / "transactions_excel.xlsx")

    try:

        # Читаем Excel-файл
        df = pd.read_excel(file_path_excel)

        # Преобразуем DataFrame в список словарей, где каждый словарь соответствует записи
        return cast(List[Dict[str, Any]], df.to_dict("records"))

    except Exception as e:
        # Обрабатываем любые возникшие ошибки и выводим информативное сообщение
        print(f"Произошла ошибка при обработке Excel-файла: {e}")

        return []
