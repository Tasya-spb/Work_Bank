import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency_valid(transactions_data):
    """Проверка корректной фильтрации по USD."""
    result = list(filter_by_currency(transactions_data, "USD"))
    # Исправлено: в ваших данных 3 транзакции USD
    assert len(result) == 3
    assert result[0]["id"] == 939719570


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 3),  # Исправлено с 2 на 3
    ("RUB", 2),  # Исправлено с 1 на 2
    ("EUR", 0),
])
def test_filter_by_currency_parametrized(transactions_data, currency, expected_count):
    """Параметризованная проверка фильтрации."""
    result = list(filter_by_currency(transactions_data, currency))
    assert len(result) == expected_count


def test_transaction_descriptions_valid(transactions_data):
    """Проверка получения описаний."""
    descriptions = transaction_descriptions(transactions_data)
    # Проверяем первые три описания из вашего списка
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


@pytest.mark.parametrize("start, end, expected_first", [
    (1, 2, "0000 0000 0000 0001"),
    (999, 999, "0000 0000 0000 0999"),
])
def test_card_number_generator_parametrized(start, end, expected_first):
    """Проверка генератора номеров карт."""
    generator = card_number_generator(start, end)
    assert next(generator) == expected_first


@pytest.fixture
def transactions_data():
    """Ваши актуальные данные из лога ошибок."""
    return [
        {"id": 939719570, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 142264268, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод со счета на счет"},
        {"id": 895315941, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод с карты на карту"},
        {"id": 873106923, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод со счета на счет"},
        {"id": 594226727, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод организации"}
    ]
