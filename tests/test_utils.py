from unittest.mock import patch, mock_open
from src.utils import get_transactions_from_json


def test_get_transactions_valid():
    """Тест успешного чтения корректного JSON-списка."""
    mock_data = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with patch("os.path.exists", return_value=True):
            assert get_transactions_from_json("data/operations.json") == [{"id": 1, "amount": 100}]


def test_get_transactions_not_found():
    """Тест случая, когда файл отсутствует."""
    with patch("os.path.exists", return_value=False):
        assert get_transactions_from_json("non_existent.json") == []


def test_get_transactions_invalid_json():
    """Тест случая, когда файл содержит некорректный JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("os.path.exists", return_value=True):
            assert get_transactions_from_json("bad.json") == []


def test_get_transactions_not_a_list():
    """Тест случая, когда в JSON не список, а словарь."""
    with patch("builtins.open", mock_open(read_data='{"id": 1}')):
        with patch("os.path.exists", return_value=True):
            assert get_transactions_from_json("not_list.json") == []
