import pytest
import requests
from unittest.mock import patch, MagicMock
from src.external_api import convertation_currency

@patch('src.external_api.api_key', 'fake_key')
@patch('src.external_api.URL', 'https://fake-url.com')
@patch('src.external_api.requests.get')


def test_convertation_currency_success(mock_get):
    """Тест успешной конвертации USD в RUB через API."""
    mock_response_data = {
        "Valute": {
            "USD": {
                "Value": 75.0,
                "Nominal": 1
            }
        }
    }

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_response_data
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    result = convertation_currency(transaction)

    assert result == 7500.0
    assert isinstance(result, float)
    mock_get.assert_called_once()


@patch('src.external_api.api_key', 'fake_key')
@patch('src.external_api.URL', 'https://fake-url.com')
@patch('src.external_api.requests.get')


def test_convertation_currency_failure(mock_get):
    """Тест обработки ошибки сети (должен вернуться 0.0 float)."""
    # Имитируем падение сети или ошибку сервера
    mock_get.side_effect = requests.RequestException("Ошибка сервера")

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    result = convertation_currency(transaction)

    # По ТЗ при ошибке строго возвращаем 0.0 типа float
    assert result == 0.0
    assert isinstance(result, float)

@patch('src.external_api.api_key', 'fake_key')
@patch('src.external_api.URL', 'https://fake-url.com')
def test_convertation_currency_RUB():
    """Тест транзакции в рублях (возврат суммы без запроса к API)."""
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }

    result = convertation_currency(transaction)
    assert result == 100.50
    assert isinstance(result, float)


















# from unittest.mock import patch
# import requests
#
# from src.external_api import convertation_currency
#
# def test_convertation_currency_success():
#     """Тест проверяет работу функции, подставляя правильные данные"""
#     mock_response_data = {
#         'Valute':{
#             'USD':{
#                 'Value':75.0,
#                 'Nominal':1
#             }
#         }
#     }
#     transaction = {
#         'operationAmount':{
#             'amount':'100',
#             'currency':{'code':'USD'}
#         }
#     }
#     with patch('src.external_api.requests.get') as mock_get:
#         mock_response = mock_get.return_value
#         mock_response.status_code = 200
#         mock_response.json.return_value = mock_response_data
#         mock_response.raise_for_status.return_value = None
#
#         result = convertation_currency(transaction)
#         assert result == 7500.0
#         mock_get.assert_called_once()
#
#
# def test_convertation_currency_failure():
#     transaction = {
#         'operationAmount':{
#             'amount':'100',
#             'currency':{'code':'USD'}
#         }
#     }
#     with patch('src.external_api.requests.get') as mock_get:
#         mock_get.return_value.raise_for_status.side_effect = requests.RequestException("Ошибка сервера")
#         result = convertation_currency(transaction)
#         assert result == 0.0
#
# def test_convertation_currensy_RUB():
#     mock_response_data = {
#         'operationAmount': {
#             'amount': '100.0',
#             'currency': {'code': 'RUB'}
#         }
#     }
#     result = convertation_currency(mock_response_data)
#     assert result == 100.0
