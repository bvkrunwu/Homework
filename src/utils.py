import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

# Настройка базового логгера для модуля
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создаём файловый хэндлер (обработчик, который записывает логи в файл)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер, определяющий структуру каждого логического сообщения
formatter = logging.Formatter("{asctime} - {name} - {levelname}: {message}", style="{")

# Присваиваем форматтер нашему файловому хэндлеру
file_handler.setFormatter(formatter)

# Подключаем хэндлер к логгеру
logger.addHandler(file_handler)


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
    # Логируем запуск функции
    logger.info("Начало работы функции")

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
                # Логируем успешную загрузку данных
                logger.info(f"Транзакции успешно загружены из файла {file_path}")

                # Если да, возвращаем полученный список транзакций
                return data_from_json

            else:
                # Предупреждение о неправильном формате данных
                logger.warning(f"Неверный формат данных в файле {file_path}")

                # Иначе выводим предупреждение о несоответствии формата данных
                print(f"Внимание: файл {file_path} содержит данные неверного формата.")

                # Возвращаем пустой список в случае некорректного формата данных
                return []

    except FileNotFoundError:
        # Логируем отсутствие файла
        logger.warning(f"Файл {file_path} не найден")

        # Обрабатываем исключение, возникающее при отсутствии файла
        print(f"Внимание: файл {file_path} не найден.")

        # Возвращаем пустой список, если файл не найден
        return []

    except json.JSONDecodeError:
        # Логируем ошибку парсинга JSON
        logger.error(f"Ошибка парсинга JSON данных в файле {file_path}")

        # Обрабатываем исключение, связанное с невозможностью распарсить JSON
        print(f"Внимание: ошибка парсинга JSON-данных в файле {file_path}.")

        # Возвращаем пустой список при ошибке парсинга JSON
        return []

    except Exception as e:
        # Логируем прочие непредвиденные ошибки
        logger.error(f"Непредвиденная ошибка при чтении файла {file_path}")

        # Обрабатываем остальные непредвиденные исключения
        print(f"Возникла непредвиденная ошибка: {e}")

        # Возвращаем пустой список при прочих ошибках
        return []

    finally:
        # Завершаем логирование независимо от успеха или неудачи
        logger.info("Завершение работы функции")
