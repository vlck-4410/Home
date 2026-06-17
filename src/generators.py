def filter_by_currency(list_dict, x=None):
    """Функция принимает на вход список словарей и маркер валюты, поочередно выдает транзакции
    где валюта операции соответствует заданной в переменной 'x'"""
    if x is None:
        yield "Нет данных"


    if not list_dict:
        yield "Нет данных"


    found_any = False

    for transaction in list_dict:
        try:
            currency_code = transaction.get('currency_code')                        #"operationAmount", {}).get("currency", {}).get("code", {})
            if currency_code == x:
                yield transaction
                found_any = True
        except TypeError, AttributeError:
            continue
    if not found_any:
        yield "Нет данных"


def transaction_descriptions(list_dict):
    """Принимает список словарей и возвращает описание каждой операции по очереди"""
    if not list_dict:
        yield "Данные отсутствуют"

    for list_ in list_dict:
        if list_.get("description", "") == "":
            yield "Данные отсутствуют"

    for description in list_dict:
        try:
            yield description.get("description", "")
        except TypeError:
            continue


def card_number_generator(start_number, end_number):
    """Принимает на вход два параметра: начальное число и конечное,
    в этом диапазоне генерирует номер карты в формате 'XXXX XXXX XXXX XXXX'"""
    if start_number == 0 or end_number == 0:
        yield "Введите значения"
        return

    for n in range(start_number, end_number + 1):
        card_number = f"{n:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"


i = filter_by_currency([{
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "\u0421\u0447\u0435\u0442 58803664561298323391",
        "to": "\u0421\u0447\u0435\u0442 39745660563456619397",
        "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438"
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u0441 \u043a\u0430\u0440\u0442\u044b \u043d\u0430 \u043a\u0430\u0440\u0442\u0443"
    }], 'PEN')
print(*i)