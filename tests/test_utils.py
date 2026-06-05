from unittest.mock import patch, mock_open
import json
from src.utils import transactions_list
import os

def test_transactions_list_success_with_patch():
    mock_transcriptions = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                            "operationAmount":{"amount":"31957.58", "currency":{"name": "руб.", "code": "RUB"}}}]
    json_string = json.dumps(mock_transcriptions)

    with patch('src.utils.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json_string)):
            result = transactions_list('fake_path/operations.json')
    assert result == mock_transcriptions


def test_transactions_list_file_not_found():
    with patch('src.utils.os.path.exists', return_value=False):
        result = transactions_list('fake_path/operations.json')
        assert result == []

def test_transactions_list_invalid_json_with_patch():
    broken_json_string = "я не json"
    with patch('src.utils.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=broken_json_string)):
            result = transactions_list('fake_path/operations.json')
            assert result == []



