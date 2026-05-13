import pytest

@pytest.fixture
def card_number():
    return '541612132155489121'

def account():
    return '551203565233543'

def mask_account_and_card():
    return (['MasterCard 545451521321864'], ['Счет 541123164512368'])