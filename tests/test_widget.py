import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value,expected', [
    ('MasterCard 2145435245643653','MasterCard 2145 43** **** 3653'),
    ('Visa 114354325435325676547', 'Visa 1143 54** **** 6547'),
    ('Visa 2143543', 'Неверные данные'),
    ('Мир 72568342576328457692384', 'Мир 7256 83** **** 2384'),
    ('Счет 123456789', 'Счет **6789'),
    ('Счет 12','Неверные данные' ),
    ('','Введите данные карты/счета'),
    ('Строка', 'Введите данные карты/счета')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('value,expected', [
    ('2024-03-11T02.23.17.325415','11.03.2024'),
    ('20=2144123','Некорректно введена дата'),
    ('','Некорректно введена дата')
])
def test_get_date(value, expected):
    assert get_date(value) == expected