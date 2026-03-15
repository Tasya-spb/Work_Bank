from src.masks import get_mask_account, get_mask_card_number

from datetime import datetime


def mask_account_card(num_for_mask: str) -> str:
    """Функция маскирует номер карты или счета"""
    num_for_mask_split = num_for_mask.split()

    if "Счет" in num_for_mask_split:
        # Номер счета обычно идет сразу после слова "Счет"
        return f"Счет {get_mask_account(num_for_mask_split[-1])}"
    else:
        card_num = []
        card_name = []
        for i in num_for_mask_split:
            if i.isdigit():
                card_num.append(i)
            else:
                card_name.append(i)

        # Собираем номер в одну строку без пробелов для функции маскировки
        str_card_num = "".join(card_num)
        str_card_name = " ".join(card_name)
        return f"{str_card_name} {get_mask_card_number(str_card_num)}"


def get_data(my_data: str) -> str:
    """Преобразует дату в формат 'ДД.ММ.ГГГГ'"""
    data_time = datetime.strptime(my_data, "%Y-%m-%dT%H:%M:%S.%f")
    return data_time.strftime("%d.%m.%Y")


# Блок для проверки работы кода
if __name__ == "__main__":
    print(get_data("2024-03-11T02:26:18.671407"))
    # Передаем реальные данные в функцию
    print(mask_account_card("Visa Gold 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))