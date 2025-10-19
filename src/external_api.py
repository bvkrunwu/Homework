import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_transaction_amount_to_rubles(transaction: dict[str, Any]) -> float | None:

    # Получаем валюту транзакции
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # Если валюта не USD или EUR, возвращаем исходную сумму
    if currency_code not in ["USD", "EUR"]:
        return float(transaction["operationAmount"]["amount"])

    # Формируем данные для запроса к API
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": transaction["operationAmount"]["amount"], "from": currency_code, "to": "RUB"}
    headers = {"apikey": os.getenv("EXCHANGE_RATES_API_KEY")}

    try:
        # Отправляем GET-запрос к API
        response = requests.get(url, headers=headers, params=payload)

        # Проверяем успешность запроса
        response.raise_for_status()

        # Возвращаем результат конвертации
        response_json: Dict[str, Any] = response.json()
        return float(response_json["result"])

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Обрабатываем ошибку HTTP

        return None

    except Exception as err:
        print(f"Other error occurred: {err}")  # Обрабатываем остальные ошибки

        return None
