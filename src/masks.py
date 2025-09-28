def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя видимым только начало и конец номера.

    Args:
        card_number (str): Номер банковской карты длиной 16 цифр.

    Returns:
        str: Отформатированная версия номера карты формата "XXXX XX** **** XXXX".

    Raises:
        ValueError: Выбрасывается,
        если передан неверный формат номера карты (не строка, не цифра или длина не равна 16).
    """
    # Проверка на пустоту строки
    if len(card_number.strip()) == 0:
        raise ValueError("Ошибка: пустой номер карты.")

    # Проверка типа и длины входящего параметра
    if not isinstance(card_number, str) or len(card_number) != 16:
        raise ValueError("Ошибка: неверная длина номера карты.")

    # Проверка на наличия числа в строке
    if not card_number.isdigit():
        raise ValueError("Ошибка: неверный формат номера карты.")

    # Формирование замаскированной строки номера карты
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя видимой только последнюю часть номера.

    Args:
        account_number (str): Номер банковского счета минимальной длиной 4 символа.

    Returns:
        str: Замаскированная версия номера счета формата "**XXXX".

    Raises:
        ValueError: Выбрасывается, если передан неверный формат номера счета (не строка, не цифра или длина менее 4).
    """
    # Проверка на пустоту строки
    if len(account_number.strip()) == 0:
        raise ValueError("Ошибка: пустой номер счета.")

    # Проверка типа и длины входящего параметра
    if not isinstance(account_number, str) or len(account_number) < 4:
        raise ValueError("Ошибка: недостаточная длина номера счета.")

    # Проверка на цифирность
    if not account_number.isdigit():
        raise ValueError("Ошибка: неверный формат номера счета.")

    # Формирование замаскированной строки номера счета
    masked_account_number = f"**{account_number[-4:]}"

    return masked_account_number
