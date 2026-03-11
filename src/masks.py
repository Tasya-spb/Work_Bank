from typing import Union


def get_user_card_number() -> str:
    """Получает номер карты от пользователя."""
    return input("Введите номер карты (ровно 16 цифр): ")


def get_valid_card_number() -> str:
    """
    Запрашивает у пользователя номер карты до тех пор, пока не будет введён корректный 16‑значный номер.

    Returns:
        str: Корректный 16‑значный номер карты
    """
    while True:
        card_number = get_user_card_number()

        if len(card_number) == 16 and card_number.isdigit():
            print("Номер карты принят")
            return card_number
        else:
            print("Ошибка: номер карты должен содержать ровно 16 цифр")


def get_mask_card_number(card_number: str) -> str:
    """Маскирует
    номер
    карты, оставляя
    видимыми
    первые
    7
    и
    последние
    4
    цифры.

    Args:
    card_number(str): 16‑значный
    номер
    карты


Returns:
str: Замаскированный
номер
в
формате
XXXXXXX ** ** XXXX

Raises:
ValueError: Если
длина
номера ≠ 16
или
строка
не
состоит
из
цифр
"""
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    if len(card_number) != 16:
        raise ValueError(f"Ошибка: номер карты должен содержать ровно 16 цифр, получено {len(card_number)}")

# Маскируем цифры с 8 по 12 (индексы 7–11)
    masked_part = "*****"
    return f"{card_number[:7]} {masked_part} {card_number[-4:]}"

# Пример использования
if __name__ == "__main__":
    try:
        valid_card = get_valid_card_number()
        masked = get_mask_card_number(valid_card)
        print(f"Замаскированный номер: {masked}")
    except ValueError as e:
        print(f"Ошибка: {e}")
"""функция маскировки номера банковской карты"""



def get_valid_account_number() -> str:
    """
    Запрашивает у пользователя номер счёта до тех пор, пока не будет введён корректный 20‑значный номер.

    Returns:
        str: Корректный 20‑значный номер счёта
    """
    while True:
        number_account = input("Введите номер счёта (ровно 20 цифр): ").strip()

        if len(number_account) != 20:
            print(f"Ошибка: номер счёта должен содержать ровно 20 цифр, а не {len(number_account)}")
            continue

        if not number_account.isdigit():
            print("Ошибка: номер счёта должен содержать только цифры")
            continue

        print("Номер счёта принят")
        return number_account

def get_mask_account(account_number: str) -> str:
    """
    Маскирует последние 4 цифры номера счёта.
    Оставляет видимыми первые 16 цифр, последние 4 заменяет на '****'.

    Args:
        account_number (str): 20‑значный номер счёта

    Returns:
        str: Замаскированный номер счёта в формате XXXXXXXXXXXXXXXXXX****

    Raises:
        ValueError: Если длина номера ≠ 20 или строка не состоит из цифр
    """
    if not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    if len(account_number) != 20:
        raise ValueError(f"Ошибка: номер счёта должен содержать ровно 20 цифр, получено {len(account_number)}")

    return f"{account_number[:16]}****"

# Пример использования

if __name__ == "__main__":
    try:
        valid_account = get_valid_account_number()
        masked_account = get_mask_account(valid_account)
        print(f"Замаскированный номер счёта: {masked_account}")
    except ValueError as e:
        print(f"Ошибка: {e}")