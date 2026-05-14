import pytest

@pytest.fixture
def card():
    return '1284723930465822'

@pytest.fixture
def account():
    return '98687557658789078769'


@pytest.fixture
def card_number():
    return 'MasterCard 8736589135087164'

@pytest.fixture
def account_name():
    return 'Счет 3243542363'

@pytest.fixture
def date():
    return '2014-02-11T02.23.17.325546'