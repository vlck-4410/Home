import pytest
import json
from src.filter_bank_operations import process_bank_search, process_bank_operations
from unittest.mock import patch, mock_open

def test_process_bank_search_success():
    mock_file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    mock_search = 'Перевод организации'
    with patch('builtins.open', mock_open(read_data=json.dumps(mock_file))):
        result = process_bank_search(mock_file, mock_search)
    assert result == mock_file


def test_process_bank_search_not_success():
    with patch('os.path.exists', return_value=False):
        result = process_bank_search('', '')
        assert result == []


def test_process_bank_operations_success():
    mock_file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    ]

    categories = ['Перевод организации', 'Открытие вклада']
    result = process_bank_operations(mock_file, categories)
    expected_result = {
        'Перевод организации': 2,
        'Открытие вклада': 1
    }
    assert result ==  expected_result


def test_process_bank_operations_not_success():
    mock_file = []
    categories = []
    expected_result = {}
    result = process_bank_operations(mock_file, categories)
    assert result == expected_result

