import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency_valid(transactions_data):
    """Проверка корректной фильтрации по USD."""
    result = list(filter_by_currency(transactions_data, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["operationAmount"]["currency"]["code"] == "USD"

def test_filter_by_currency_empty_list():
    """Проверка работы с пустым списком."""
    result = list(filter_by_currency([], "USD"))
    assert result == []

def test_filter_by_currency_no_match(transactions_data):
    """Проверка случая, когда искомой валюты нет."""
    result = list(filter_by_currency(transactions_data, "EUR"))
    assert result == []

# --- Тесты для transaction_descriptions ---

def test_transaction_descriptions_valid(transactions_data):
    """Проверка получения всех описаний."""
    descriptions = transaction_descriptions(transactions_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"

def test_transaction_descriptions_empty():
    """Проверка генератора описаний на пустом списке."""
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []

# --- Тесты для card_number_generator ---

def test_card_number_generator_range():
    """Проверка диапазона и формата (ведущие нули и пробелы)."""
    generator = card_number_generator(1, 3)
    results = list(generator)
    assert results == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]

def test_card_number_generator_single_value():
    """Проверка крайних значений (одно и то же число)."""
    generator = card_number_generator(999, 999)
    assert next(generator) == "0000 0000 0000 0999"
    with pytest.raises(StopIteration):
        next(generator)

# --- Фикстура с данными для тестов ---

@pytest.fixture
def transactions_data():
    return [
        {
            "id": 939719570,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации"
        },
        {
            "id": 142264268,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод со счета на счет"
        },
        {
            "id": 895315941,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет"
        }
    ]
