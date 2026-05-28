import pytest
from src.generators import *



def test_generator_transaction_descriptions(currency_to_filter):
   test_data = currency_to_filter
   expected_results = ['Перевод организации',
        'Перевод со счета на счет',
        'Перевод со счета на счет',
        'Перевод с карты на карту',
        'Перевод организации']
   generator = transaction_descriptions(test_data)
   for expected in expected_results:
       assert next(generator) == expected


def test_generator_transaction_descriptions_zero_data():
    test_data = ([])
    generator = transaction_descriptions(test_data)
    expected_results = ['Данные отсутствуют']
    for expected in expected_results:
        assert next(generator) == expected


def test_generator_transaction_descriptions_less_key_description(less_key_transaction):
    test_data = less_key_transaction
    generator = transaction_descriptions(test_data)
    expected_results = ['Данные отсутствуют',
                        'Данные отсутствуют',
                        'Данные отсутствуют',
                        'Данные отсутствуют',
                        'Перевод организации']
    for expected in expected_results:
        assert next(generator) == expected


def test_filter_by_currency_zero_data():
    test_data = ([])
    generator = filter_by_currency(test_data)
    expected_results = ['Нет данных']
    for expected in expected_results:
        assert next(generator) == expected


def test_filter_by_currency_zero_data_with_currency():
    test_data = ([])
    generator = filter_by_currency(test_data)
    expected_results = ['Нет данных']
    for expected in expected_results:
        assert next(generator) == expected


def test_filter_by_currency_less_key_data(currency_less_key_data):
    test_data = currency_less_key_data

    generator = filter_by_currency(test_data, "RUB")
    expected_results = ['Нет данных']
    for expected in expected_results:
        assert next(generator) == expected


@pytest.mark.parametrize('start_number, end_number, expected', [
    (0, 0,['Введите значения']),
    (1, 5, ['0000 0000 0000 0001',
                        '0000 0000 0000 0002',
                        '0000 0000 0000 0003',
                        '0000 0000 0000 0004',
                        '0000 0000 0000 0005']),
     (1, 1, ['0000 0000 0000 0001'])
 ])
def test_card_number_generator(start_number, end_number, expected):
    assert list(card_number_generator(start_number, end_number)) == expected




