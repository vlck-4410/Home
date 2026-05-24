def filter_by_currency(list_dict, x=None):
    """Функция принимает на вход список словарей и маркер валюты, поочередно выдает транзакции
    где валюта операции соответствует заданной в переменной 'x'"""
    if x is None:
        yield "Нет данных"
        return

    if not list_dict:
        yield "Нет данных"
        return

    found_any = False

    for transaction in list_dict:
        try:
            currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
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
