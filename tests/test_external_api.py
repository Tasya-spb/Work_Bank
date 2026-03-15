from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount_in_rub


@patch("src.external_api.requests.get")
def test_get_amount_usd_conversion(mock_get):
    """Тест конвертации USD в RUB через API."""
    # Настраиваем Mock-ответ от сервера
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    result = get_transaction_amount_in_rub(transaction)
    assert result == 7500.0
    mock_get.assert_called_once()  # Проверяем, что запрос действительно был отправлен


def test_get_amount_rub_no_api():
    """Тест транзакции в рублях (API не должно вызываться)."""
    transaction = {
        "operationAmount": {
            "amount": "500.0",
            "currency": {"code": "RUB"}
        }
    }
    # Если функция вызовет API, тест упадет, так как мы не пропатчили requests
    assert get_transaction_amount_in_rub(transaction) == 500.0


@patch("src.external_api.requests.get")
def test_get_amount_api_error(mock_get):
    """Тест поведения при ошибке API (возврат 0.0)."""
    mock_get.side_effect = Exception("API Connection Error")

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"}
        }
    }
    assert get_transaction_amount_in_rub(transaction) == 0.0
