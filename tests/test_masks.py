from unittest.mock import patch

import pytest

from src.masks import (get_mask_account, get_mask_card_number,
                       get_user_card_number, get_valid_account_number)

# --- ТЕСТЫ МАСКИРОВКИ (Чистые функции) ---

@pytest.mark.parametrize("card, expected", [
    ("1234567890123456", "1234567*****3456"),
])
def test_get_mask_card_number_success(card, expected):
    assert get_mask_card_number(card) == expected

@pytest.mark.parametrize("invalid", ["123", "abc1234567890123", ""])
def test_get_mask_card_number_errors(invalid):
    with pytest.raises(ValueError, match="ровно 16 цифр"):
        get_mask_card_number(invalid)

@pytest.mark.parametrize("acc, expected", [
    ("12345678901234567890", "1234567890123456****"),
])
def test_get_mask_account_success(acc, expected):
    assert get_mask_account(acc) == expected

@pytest.mark.parametrize("invalid", ["123", "abc", "1" * 21])
def test_get_mask_account_errors(invalid):
    with pytest.raises(ValueError, match="ровно 20 цифр"):
        get_mask_account(invalid)

# --- ТЕСТЫ ВВОДА (Имитация пользователя через patch) ---

def test_get_user_card_number_valid():
    """Эмулируем ввод: сначала ошибка, потом верный номер"""
    with patch('builtins.input', side_effect=["123", "1234567890123456"]):
        assert get_user_card_number() == "1234567890123456"

def test_get_valid_account_number_valid():
    """Эмулируем ввод: сначала буквы, потом неверная длина, потом успех"""
    with patch('builtins.input', side_effect=["abc", "123", "12345678901234567890"]):
        assert get_valid_account_number() == "12345678901234567890"

def test_get_user_card_number_full_coverage():
    """Неверная длина, 2. Буквы, 3. Верный номер"""
    inputs = ["123", "abc1234567890123", "1234567890123456"]
    with patch('builtins.input', side_effect=inputs):
        assert get_user_card_number() == "1234567890123456"

def test_get_valid_account_number_full_coverage():
    """"Неверная длина, 2. Буквы вместо цифр, 3. Верный номер"""""
    inputs = ["123", "123456789012345678ab", "12345678901234567890"]
    with patch('builtins.input', side_effect=inputs):
        assert get_valid_account_number() == "12345678901234567890"