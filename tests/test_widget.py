import pytest
from datetime import datetime
from src.widget import mask_account_card, get_data


# Тесты для функции mask_account_card
@pytest.mark.parametrize("input_data, expected", [
    # Проверка карт
    ("Visa Gold 7000792289606361", "Visa Gold 7000792*****6361"),
    ("MasterCard 7158300734726758", "MasterCard 7158300*****6758"),
    ("Maestro 1596837493215942", "Maestro 1596837*****5942"),
    # Проверка счета
    ("Счет 73654108430135874305", "Счет 7365410843013587****"),
    ("Счет 12345678901234567890", "Счет 1234567890123456****"),
])
def test_mask_account_card_valid(input_data, expected):
    """Проверка корректной маскировки разных типов карт и счетов"""
    assert mask_account_card(input_data) == expected

def test_mask_account_card_empty():
    """Проверка устойчивости к пустым входным данным"""
    with pytest.raises(Exception): # Или укажите конкретную ошибку, которую выдает ваш код
        mask_account_card("")

# Тесты для функции get_data
@pytest.mark.parametrize("input_date, expected_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-12-31T23:59:59.999999", "31.12.2025"),
    ("2023-01-01T00:00:00.000000", "01.01.2023"),
])
def test_get_data_format(input_date, expected_date):
    """Проверка корректного преобразования формата даты"""
    assert get_data(input_date) == expected_date

def test_get_data_invalid_format():
    """Проверка обработки некорректной строки даты"""
    with pytest.raises(ValueError):
        get_data("11.03.2024") # Неверный входной формат