import os
from unittest.mock import MagicMock, patch

from src.tranzacziione import get_transactions_from_csv, get_transactions_from_excel


# 1. Тестирование CSV
@patch("src.tranzacziione.os.path.exists")
@patch("builtins.open")
@patch("src.tranzacziione.csv.DictReader")
def test_get_transactions_from_csv(mock_dict_reader, mock_open, mock_exists):
    """Тест успешного чтения CSV через Mock."""
    # Имитируем, что файл существует
    mock_exists.return_value = True

    # Настраиваем Mock для DictReader
    mock_dict_reader.return_value = [
        {"id": "1", "amount": "100.0", "currency": "RUB"},
        {"id": "2", "amount": "200.0", "currency": "USD"}
    ]

    result = get_transactions_from_csv("fake_path.csv")

    assert len(result) == 2
    assert result[0]["amount"] == "100.0"
    mock_open.assert_called_once_with("fake_path.csv", mode="r", encoding="utf-8")


# 2. Тестирование Excel
@patch("src.tranzacziione.pd.read_excel")
@patch("src.tranzacziione.os.path.exists")
def test_get_transactions_from_excel(mock_exists, mock_read_excel):
    """Тест успешного чтения Excel через Mock."""
    # Имитируем наличие файла
    mock_exists.return_value = True

    # Создаем фиктивный DataFrame (имитируем цепочку fillna().to_dict())
    mock_df = MagicMock()
    expected_data = [{"id": 6527058, "state": "EXECUTED", "amount": 1621.0}]
    mock_df.fillna.return_value = mock_df
    mock_df.to_dict.return_value = expected_data

    mock_read_excel.return_value = mock_df

    result = get_transactions_from_excel("data/transactions_excel.xlsx")

    assert result == expected_data
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")


# 3. Тесты на ошибки (файлы не найдены)
def test_get_transactions_csv_not_found():
    """Тест возврата пустого списка, если файл CSV отсутствует."""
    with patch("src.tranzacziione.os.path.exists", return_value=False):
        assert get_transactions_from_csv("missing.csv") == []


def test_get_transactions_excel_not_found():
    """Тест возврата пустого списка, если файл Excel отсутствует."""
    with patch("src.tranzacziione.os.path.exists", return_value=False):
        assert get_transactions_from_excel("missing.xlsx") == []