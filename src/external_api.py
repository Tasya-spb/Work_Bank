import os
import requests
from dotenv import load_dotenv
from typing import Any, Dict

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


def get_transaction_amount_in_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях (float).
    Если валюта USD/EUR, запрашивает курс через Exchange Rates Data API.
    """
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"] and API_KEY:
        url = f"https://api.apilayer.com{currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            result = response.json()
            return float(result.get("result", 0.0))
        except (requests.RequestException, ValueError):
            return 0.0

    return 0.0
