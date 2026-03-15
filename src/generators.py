from typing import Any, Dict, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> iter:
    """Возвращает итератор с транзакциями в указанной валюте."""
    return (
        transaction for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )


def transaction_descriptions(transactions):
    """Генератор, который поочередно возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, stop):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, stop + 1):
        # Форматируем число: 16 знаков с ведущими нулями
        card_str = f"{number:016}"
        # Разделяем строку на блоки по 4 символа через пробел
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
for card_number in card_number_generator(1, 5):
    print(card_number)
