import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize('value,expected', [
    ('12345678910111213','**1213' ),
    ('','Некорректно введены данные счета'),
    ('0','Некорректно введены данные счета')
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize('value,expected', [
    ('32576385764328572364','3257 63** **** 2364'),
    ('51256','Неправильный номер карты'),
    ('0', 'Неправильный номер карты'),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


def test_mask_account_fixture(account):
    assert get_mask_account(account) == '**8769'

def test_card_number_fixture(card):
    assert get_mask_card_number(card) == '1284 72** **** 5822'

