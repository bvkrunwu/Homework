import logging

# Настройка базового логгера для модуля
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создаём файловый хэндлер (обработчик, который записывает логи в файл)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер, определяющий структуру каждого логического сообщения
formatter = logging.Formatter("{asctime} - {name} - {levelname}: {message}", style="{")

# Присваиваем форматтер нашему файловому хэндлеру
file_handler.setFormatter(formatter)

# Подключаем хэндлер к логгеру
logger.addHandler(file_handler)


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
    try:
        # Логируем начало работы функции
        logger.info("Начало работы функции")
        # Проверяем наличие переданного значения
        if len(card_number.strip()) == 0:
            # Логируем ошибку пустого номера карты
            logger.error(f"Ошибка: пустой номер карты '{card_number}'")
            raise ValueError("Ошибка: пустой номер карты.")

        # Проверяем длину и валидность формата карты
        if not isinstance(card_number, str) or len(card_number) != 16:
            # Логируем ошибку длины номера карты
            logger.error(f"Ошибка: неверная длина номера карты '{card_number}'")
            raise ValueError("Ошибка: неверная длина номера карты.")

        # Проверяем на наличия числа в строке
        if not card_number.isdigit():
            # Логируем ошибку формата номера карты
            logger.error(f"Ошибка: неверный формат номера карты '{card_number}'")
            raise ValueError("Ошибка: неверный формат номера карты.")

        # Формируем маскированный номер карты
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        # Логируем успешное маскирование номера карты
        logger.info(f"Успешно замаскирован номер карты '{masked_card_number}'")

        # Логируем завершение работы функции
        logger.info("Завершение работы функции")
        return masked_card_number

    except Exception as e:
        # Логируем возникшую ошибку при обработке номера карты
        logger.error(f"Произошла ошибка при обработке номера карты '{card_number}': {e}")
        raise


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
    try:
        # Логируем начало работы функции
        logger.info("Начало работы функции")

        # Проверяем наличие переданного значения
        if len(account_number.strip()) == 0:
            # Логируем ошибку пустого номера счета
            logger.error(f"Ошибка: пустой номер счета '{account_number}'")
            raise ValueError("Ошибка: пустой номер счета.")

        # Проверяем тип и длину входящего параметра
        if not isinstance(account_number, str) or len(account_number) < 4:
            # Логируем ошибку длины номера счета
            logger.error(f"Ошибка: недостаточная длина номера счета '{account_number}'")
            raise ValueError("Ошибка: недостаточная длина номера счета.")

        # Проверяем, что номер счёта состоит только из цифр.
        if not account_number.isdigit():
            # Логируем ошибку формата номера счета
            logger.error(f"Ошибка: неверный формат номера счета '{account_number}'")
            raise ValueError("Ошибка: неверный формат номера счета.")

        # Формирование замаскированной строки номера счета
        masked_account_number = f"**{account_number[-4:]}"
        # Логируем успешное маскирование номера счета
        logger.info(f"Успешно замаскирован номер счёта '{masked_account_number}'")

        # Логируем завершение работы функции
        logger.info("Завершение работы функции")
        return masked_account_number

    except Exception as e:
        # Логируем возникшую ошибку при обработке номера счета
        logger.error(f"Произошла ошибка при обработке номера счёта '{account_number}': {e}")
        raise
