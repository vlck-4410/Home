from unittest.mock import patch, mock_open
import pandas as pd
from src.read_file import read_file_csv, read_file_excel

def test_read_file_csv_not_succses():
    csv_data = 'id,state,amount\n1,EXECUTED,100.0\n2,CANSELED,200.0'
    with patch('builtins.open', mock_open(read_data=csv_data)) as mock_file:
        result = read_file_csv('fake_path.csv')
        assert result == [
            {'id': '1', 'state': 'EXECUTED', 'amount': '100.0'},
            {'id': '2', 'state': 'CANSELED', 'amount': '200.0'},
        ]
        mock_file.assert_called_once()

def test_read_file_csv_not_succses():
    with patch('builtins.open', side_effect=FileNotFoundError) :
        result = read_file_csv('missing_file.csv')
        assert result == 'Ошибка чтения файла '


def test_read_file_excel_succses():
    mock_dataframe = [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100.0},
        {'id': 2, 'state': 'CANSELED', 'amount': 200.0},
    ]
    mock_dataframe = pd.DataFrame(mock_dataframe)
    with patch('src.read_file.pd.read_excel', return_value=mock_dataframe):
        result = read_file_excel('fake_path.xlsx')
        assert result == [
            {'id': 1, 'state': 'EXECUTED', 'amount': 100.0},
            {'id': 2, 'state': 'CANSELED', 'amount': 200.0},
        ]


def test_read_file_excel_not_succses():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = read_file_excel('missing_file.xlsx')
        assert result == 'Ошибка чтения файла '

