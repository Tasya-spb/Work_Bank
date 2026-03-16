import logging
import os

# 1. Создаем объект логера для модуля masks
logger = logging.getLogger(__name__)

# 2. Устанавливаем уровень логирования не меньше DEBUG
logger.setLevel(logging.DEBUG)

# 3. Настраиваем file_handler (режим 'w' для перезаписи лога)
log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'masks.log')
os.makedirs(os.path.dirname(log_path), exist_ok=True)
file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')

# 4. Настраиваем file_formatter (метка времени, модуль, уровень, сообщение)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 5. Устанавливаем форматер для handler
file_handler.setFormatter(file_formatter)

# 6. Добавляем handler к логеру
logger.addHandler(file_handler)


def get_user_card_number() -> str:
    """ Запрашивает у пользователя номер карты до тех пор, пока не будет введён корректный 16‑значный номер.Returns:
        str: Корректный 16‑значный номер карты"""
    while True:
        card_number = input("Введите 16-значный номер карты: ")

        if len(card_number) == 16 and card_number.isdigit():
            print("Номер карты принят")
            return card_number
        else:
            print("Ошибка: номер карты должен содержать ровно 16 цифр")


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 7 и последние 4 цифры"""
    """Маскирует номер карты."""
    logger.info(f"Начало маскировки карты: {card_number}")

    if not card_number.isdigit():
        raise ValueError("Ошибка: номер карты должен содержать ровно 16 цифр")

    if len(card_number) != 16:
        raise ValueError("Ошибка: номер карты должен содержать ровно 16 цифр")
        logger.error(f"Ошибка: Некорректный номер счета '{card_number}'")
        return "Invalid account number"

# Маскируем цифры с 8 по 12 (индексы 7–11)
    masked_part = "*****"
    return (f"{card_number[:7]}{masked_part}{card_number[-4:]}")
    # Логирование успешного случая
    logger.info(f"Карта успешно замаскирована: {masked}")
    return


# Пример использования
if __name__ == "__main__":
    try:
        raw_card = get_user_card_number()
        masked = get_mask_card_number(raw_card)
        print(f"Замаскированный номер: {masked}")
    except ValueError:
        print("Ошибка: номер карты должен содержать ровно 16 цифр")
"""функция маскировки номера банковской карты"""


def get_valid_account_number() -> str:
    """Запрашивает у пользователя номер счёта до тех пор, пока не будет введён корректный 20‑значный номер.
        Returns:
            str: Корректный 20‑значный номер счёта"""
    while True:
        number_account = input("Введите номер счёта (ровно 20 цифр): ").strip()

        if len(number_account) != 20:
            print("Ошибка: номер счёта должен содержать ровно 20 цифр")
            continue

        if not number_account.isdigit():
            print("Ошибка: номер счёта должен содержать ровно 20 цифр")
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
    """Маскирует номер карты."""
    logger.info(f"Начало маскировки счета: {account_number}")

    if not account_number.isdigit():
        raise ValueError("Ошибка: номер счёта должен содержать ровно 20 цифр")
        logger.error(f"Ошибка: Некорректный номер счета '{account_number}'")

    if len(account_number) != 20:
        raise ValueError("Ошибка: номер счёта должен содержать ровно 20 цифр")

    return f"{account_number[:16]}****"

if __name__ == "__main__":
    try:
        account_number = get_valid_account_number()
        masked_account = get_mask_account(account_number)
        print(f"Замаскированный номер счёта: {masked_account}")
    except ValueError:
        print("Ошибка: номер счёта должен содержать ровно 20 цифр")
