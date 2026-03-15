import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
API_KEY = os.getenv("YOUR_API_KEY")


def get_transaction_amount_in_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях (float).
    Если валюта USD/EUR, запрашивает курс через Exchange Rates Data API.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0))
    currency = operation_amount.get("currency", {}).get("code")

    # Если валюта уже в рублях, возвращаем как есть
    if currency == "RUB":
        return amount

    # Если USD или EUR, выполняем конвертацию через API
    if currency in ["USD", "EUR"] and API_KEY:
        # ВАЖНО: Полный URL для конвертации
        url = f"https://api.apilayer.com/exchangerates_data/live?base=USD&symbols=EUR,GBP' \
--header 'apikey: YOUR API KEY {currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            result = response.json()
            return float(result.get("result", 0.0))
        except Exception:
            # В случае любой ошибки API (таймаут, неверный ключ) возвращаем 0.0
            return 0.0

            # 3. Если валюта не RUB/USD/EUR или нет ключа API
        return amoun

