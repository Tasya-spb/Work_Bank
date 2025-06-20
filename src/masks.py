from typing import Union

while True:
    card_number = input("Введите номер карты (ровно 16 цифр): ")
    """Запрос номера карты пользователя"""
    if len(card_number) == 16 and card_number.isdigit():
        print("Номер карты принят")
        break
    else:
        print("Ошибка: номер карты должен содержать ровно 16 цифр")
"""Цикл на ввод 16-ти значного номера, если нет, то выдаст ошибку"""


def get_mask_card_number(card_number: str) -> str:
    return f"{card_number[:4]}  {card_number[4:7]}**  ****  {card_number[-4:]}"


"""функция маскировки номера банковской карты"""

print(get_mask_card_number(card_number))

while True:
    number_account = input("Введите номер счета (ровно 20 цифр): ")
    """Запрос номера счета пользователя"""
    if len(number_account) == 20 and number_account.isdigit():
        print("Номер счета принят")
        break
    else:
        print("Ошибка: номер счета должен содержать ровно 16 цифр")
"""Цикл на ввод 20-ти значного номера счета"""


def get_mask_account(number_account: str) -> str:
    return f"**{number_account[16:]}"


print(get_mask_account(number_account))
