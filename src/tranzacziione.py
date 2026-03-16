import csv
import os
from typing import Any, Dict, List
import pandas as pd  # Добавлен импорт pandas


def get_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Читает транзакции из CSV."""
    transactions: List[Dict[str, Any]] = []
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                transactions.append(row)
        return transactions
    except (FileNotFoundError, csv.Error):
        return []


def get_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """Читает транзакции из Excel."""
    if not os.path.exists(file_path):
        return []
    try:
        df = pd.read_excel(file_path)
        df = df.fillna("")
        # ИСПРАВЛЕНО: return должен быть ВНУТРИ блока try
        return df.to_dict(orient="records")
    except Exception:
        return []


if __name__ == "__main__":
    # ИСПРАВЛЕНО: Поправлены отступы внутри блока main
    csv_path = "data/transactions.csv"
    excel_path = "data/transactions_excel.xlsx"

    data_from_csv = get_transactions_from_csv(csv_path)
    data_from_excel = get_transactions_from_excel(excel_path)

    print(f"Из CSV загружено: {len(data_from_csv)} строк")
    print(f"Из Excel загружено: {len(data_from_excel)} строк")
