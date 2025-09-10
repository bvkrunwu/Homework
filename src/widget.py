from .masks import get_mask_account
from .masks import get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """
    Функция принимает строку с названием карты/счета и его номером и возвращает замаскированную версию номера.

    Аргументы:
        info_string (str): Строка, содержащая название карты/счета и его номер (разделяются пробелом).

    Возвращаемое значение:
        str: Строка с замаскированной версией номера карты/счета.
    """
    # Разделяем входную строку на две части: название и номер
    account_title, account_number = info_string.rsplit(" ", 1)

    # Проверяем корректность входных данных
    if not account_title or not account_number:
        return "Ошибка: некорректный формат входной строки!"

    # Определяем тип и применяем соответствующую маску
    if account_title.lower() == "счет":
        masked_number = get_mask_account(account_number)
    else:
        masked_number = get_mask_card_number(account_number)

    # Возвращаем результат в виде строки с названием и замаскированным номером
    return f"{account_title} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Функция преобразует строку даты из формата YYYY-MM-DD в формат ДД.ММ.ГГГГ.

    Аргументы:
        date_string (str): Строка даты в формате YYYY-MM-DD.

    Возвращаемое значение:
        str: Отформатированная строка даты в формате ДД.ММ.ГГГГ.
    """
    # Разделяем входную строку на компоненты: год, месяц и день
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Формируем новую строку в нужном формате
    return f"{day}.{month}.{year}"
