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

@pytest.fixture
def filter():
    return ([{'id': 325452352, 'state': 'EXECUTED', 'date': '2015-02-03T18:35:29.515364'},{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}])

@pytest.fixture
def date_to_sort():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2017-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-06-30T02:08:58.425572'}])