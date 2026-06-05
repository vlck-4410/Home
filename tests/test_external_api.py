from unittest.mock import patch
import requests

from src.external_api import convertation_currency

def test_convertation_currency_success():
    """Тест проверяет работу функции, подставляя правильные данные"""
    mock_response_data = {
        'Valute':{
            'USD':{
                'Value':75.0,
                'Nominal':1
            }
        }
    }
    transaction = {
        'operationAmount':{
            'amount':'100',
            'currency':{'code':'USD'}
        }
    }
    with patch('src.external_api.requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        result = convertation_currency(transaction)
        assert result == 7500.0
        mock_get.assert_called_once()


def test_convertation_currency_failure():
    transaction = {
        'operationAmount':{
            'amount':'100',
            'currency':{'code':'USD'}
        }
    }
    with patch('src.external_api.requests.get') as mock_get:
        mock_get.return_value.raise_for_status.side_effect = requests.RequestException("Ошибка сервера")
        result = convertation_currency(transaction)
        assert result is None

def test_convertation_currensy_RUB():
    mock_response_data = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'RUB'}
        }
    }
    result = convertation_currency(mock_response_data)
    assert result == 100
