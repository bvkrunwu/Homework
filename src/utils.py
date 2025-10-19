from pathlib import Path

import json

from typing import Dict, List, Optional, Any


def load_transactions(file_path: Optional[str | Path]) -> Optional[List[Dict[str, Any]]]:
    """
    Функция загружает финансовые транзакции из указанного JSON-файла.

    Args:
        file_path (Optional[str | Path]): Путь к файлу JSON с финансовыми транзакциями.
            По умолчанию используется файл 'operations.json' в папке 'data'.

    Returns:
        Optional[List[Dict[str, Any]]]: Список словарей с данными транзакций,
        либо пустой список в случае ошибок или неправильного формата данных.
    """
    # Проверяем, указан ли путь к файлу. Если нет, определяем путь автоматически
    if not file_path:
        # Определяем корень проекта относительно расположения текущего файла (__file__)
        project_root = Path(__file__).resolve().parent.parent
        # Формируем полный путь к файлу операций в каталоге 'data'
        file_path = project_root / "data" / "operations.json"

    try:
        # Открываем файл в режиме чтения с указанием кодировки UTF-8
        with open(file_path, "r", encoding="utf-8") as json_file:
            # Читаем и десериализуем JSON-данные из файла
            data_from_json = json.load(json_file)

            # Проверяем, является ли прочитанная структура списком
            if isinstance(data_from_json, list):

                # Если да, возвращаем полученный список транзакций
                return data_from_json

            else:
                # Иначе выводим предупреждение о несоответствии формата данных
                print(f"Внимание: файл {file_path} содержит данные неверного формата.")

                # Возвращаем пустой список в случае некорректного формата данных
                return []

    except FileNotFoundError:
        # Обрабатываем исключение, возникающее при отсутствии файла
        print(f"Внимание: файл {file_path} не найден.")

        # Возвращаем пустой список, если файл не найден
        return []

    except json.JSONDecodeError:
        # Обрабатываем исключение, связанное с невозможностью распарсить JSON
        print(f"Внимание: ошибка парсинга JSON-данных в файле {file_path}.")

        # Возвращаем пустой список при ошибке парсинга JSON
        return []

    except Exception as e:
        # Обрабатываем остальные непредвиденные исключения
        print(f"Возникла непредвиденная ошибка: {e}")

        # Возвращаем пустой список при прочих ошибках
        return []
