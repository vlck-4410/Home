def filter_by_currency(list_dict, x=None):
    if x is None:
        yield 'Нет данных'
        return

    if not list_dict:
        yield 'Нет данных'
        return

    for transaction in list_dict:
        try:
            if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == x:
                yield transaction
        except TypeError:
            continue


def transaction_descriptions(list_dict):
    if not list_dict:
        yield 'Данные отсутствуют'

    for list_ in list_dict:
        if list_.get("description", '') == '':
            yield 'Данные отсутствуют'


    for description in list_dict:
        try:
            yield description.get("description", "")
        except TypeError:
            continue


def card_number_generator(start_number, end_number):
    return (
        f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        for num_str in (f"{n:016d}" for n in range(start_number, end_number + 1))
    )


description = filter_by_currency([{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",

                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",

                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",

                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }], x="RUB")
for x in range(1):
    print(*description)

