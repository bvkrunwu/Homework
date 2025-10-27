import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Возвращает список операций, в описании которых встречается заданная строка.

    Args:
      data: Список словарей с банковскими операциями.
      search: Строка для поиска в описании операций.

    Returns:
      Список операций, содержащих заданную строку в описании.
    """

    if not isinstance(data, list):
        raise ValueError("Параметр data должен быть списком.")

    # Компилируем регулярное выражение для поиска
    pattern = re.compile(search.lower())

    # Возвращаем список операций, у которых в описании найдена заданная строка
    return [op for op in data if pattern.search(op.get("description", ""))]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций по указанным категориям.

    Args:
      data: Список словарей с банковскими операциями.
      categories: Список категорий для поиска в описаниях операций.

    Returns:
      Словарь, где ключи — это категории, а значения — количество операций в каждой категории.
    """

    if not isinstance(data, list):
        raise ValueError("Параметр data должен быть списком.")

    # Создаем экземпляр Counter для хранения статистики по категориям
    category_counts: Counter[str] = Counter()

    # Проходим по каждому элементу данных
    for transaction in data:
        desc = transaction.get("description", "")

        # Просматриваем каждую категорию
        for cat in categories:
            if cat in desc:
                category_counts[cat] += 1

    # Преобразуем Counter обратно в обычный словарь
    return dict(category_counts)
