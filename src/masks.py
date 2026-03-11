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



while True:
    number_account = input("Введите номер счета (ровно 20 цифр): ")
    """Запрос номера счета пользователя"""
    if len(number_account) == 20 and number_account.isdigit():
        print("Номер счета принят")
        break
    else:
        print("Ошибка: номер счета должен содержать ровно 20 цифр")
"""Цикл на ввод 20-ти значного номера счета"""


def get_mask_account(number_account: str) -> str:
    return f"**{number_account[16:]}"


print(get_mask_account(number_account))
