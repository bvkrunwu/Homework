from datetime import datetime

from .masks import get_mask_account
from .masks import get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """
    Функция маскирует номер счета или банковской карты в строке формата "Label Number".

    Args:
        info_string (str): Входящая строка, содержащая метку и номер (разделённые пробелом)

    Returns:
        str: Строка с замаскированным номером счета или карты

    Raises:
        ValueError: Возбуждается, если количество частей строки отличается от двух
    """

    # Разделяем входящую строку на части по пробелу
    parts = info_string.split()

    # Проверяем, что строка состоит именно из двух частей (метка + номер)
    if len(parts) != 2:
        raise ValueError("Некорректный ввод данных")

    # Извлекаем метку и номер из частей строки
    label, number = parts

    # Определяем тип номера по метке и применяем соответствующую маску
    if label.lower().startswith("счет"):
        # Если метка начинается со слова "счет", маскируем номер как счёт
        masked_number = get_mask_account(number)
    else:
        # Иначе маскируем номер как банковскую карту
        masked_number = get_mask_card_number(number)

    # Формируем итоговую строку с замаскированным номером
    return f"{label} {masked_number}"


def get_date(iso_date_str: str) -> str:
    """
    Функция конвертирует ISO-строку даты в формат ДД.ММ.ГГГГ.

    Args:
        iso_date_str (str): Дата в формате ISO (YYYY-MM-DDTHH:MM:SS.mmmmmm)

    Returns:
        str: Отформатированная дата в виде ДД.ММ.ГГГГ

    Raises:
        ValueError: Возбуждается при невозможности распарсить входную строку
    """

    # Удаляем микросекунды из ISO-строки для корректного преобразования
    date_part = iso_date_str.rsplit(".", maxsplit=1)[0]

    # Конвертируем строку в объект datetime
    try:
        dt = datetime.fromisoformat(date_part)

        # Форматируем дату в нужный вид ДД.ММ.ГГГГ
        formatted_date = dt.strftime("%d.%m.%Y")
        return formatted_date
    except ValueError as e:
        # Генерируем ошибку с детальной информацией при неудачном парсинге
        raise ValueError(f"Ошибка парсинга даты: {e}")
