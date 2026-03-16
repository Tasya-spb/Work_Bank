import os
from src.utils import get_transactions_from_json
from src.tranzacziione import get_transactions_from_csv, get_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.masks import get_mask_card_number, get_mask_account


def format_date(date_str):
    """Преобразует ISO дату (2019-12-08T...) в формат 08.12.2019."""
    if not date_str or len(date_str) < 10:
        return "Дата неизвестна"
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"


def mask_from_to(name_number):
    """Определяет, карта это или счет, и накладывает маску."""
    if not name_number or name_number == "nan":
        return ""
    if "Счет" in name_number:
        name = "Счет"
        number = name_number.replace("Счет", "").strip()
        return f"{name} {get_mask_account(number)}"
    else:
        # Для карт: отделяем название от номера
        parts = name_number.split()
        number = parts[-1]
        name = " ".join(parts[:-1])
        return f"{name} {get_mask_card_number(number)}"


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()
    transactions = []

    # 1. Выбор файла
    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = get_transactions_from_json(os.path.join("data", "operations.json"))
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = get_transactions_from_csv(os.path.join("data", "transactions.csv"))
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = get_transactions_from_excel(os.path.join("data", "transactions_excel.xlsx"))
    else:
        print("Программа: Неверный выбор.")
        return

    # 2. Фильтрация по статусу
    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        user_status = input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).strip().upper()

        if user_status in statuses:
            transactions = filter_by_state(transactions, user_status)
            print(f'Программа: Операции отфильтрованы по статусу "{user_status}"')
            break
        else:
            print(f'Программа: Статус операции "{user_status}" недоступен.')

    # 3. Сортировка по дате
    if input("\nОтсортировать операции по дате? Да/Нет: ").strip().lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию?: ").strip().lower()
        is_reverse = True if "убыв" in order else False
        transactions = sort_by_date(transactions, reverse=is_reverse)

    # 4. Фильтр только RUB
    if input("\nВыводить только рублевые транзакции? Да/Нет: ").strip().lower() == "да":
        transactions = [
            t for t in transactions
            if (str(t.get('operationAmount', {}).get('currency', {}).get('code')) == 'RUB' or
                str(t.get('currency_code')) == 'RUB')
        ]

    # 5. Фильтр по слову
    if input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower() == "да":
        search_word = input("Введите слово для поиска: ").strip()
        transactions = process_bank_search(transactions, search_word)

    # 6. Итоговый вывод
    print("\nПрограмма: Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Программа: Всего банковских операций в выборке: {len(transactions)}\n")
        for t in transactions:
            date = format_date(t.get('date', ''))
            desc = t.get('description', 'Без описания')

            # Маскировка отправителя и получателя
            from_info = mask_from_to(str(t.get('from', '')))
            to_info = mask_from_to(str(t.get('to', '')))

            # Сумма и валюта (универсально для всех типов файлов)
            amount = t.get('operationAmount', {}).get('amount') or t.get('amount')
            currency = (t.get('operationAmount', {}).get('currency', {}).get('name') or
                        t.get('currency_name') or 'руб.')

            print(f"{date} {desc}")
            if from_info:
                print(f"{from_info} -> {to_info}")
            else:
                print(f"{to_info}")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()

