def filter_by_state(list_dict: list, state="EXECUTED") -> list:
    """Принимает список словарей и значение для ключа state, возвращает новый список,
    со словарями, в которых state соответсвтует указанному значению."""
    sorted_dict = []
    if not isinstance(list_dict, list):
        return 'Неверный тип введенных данных, ожидался список'
    else:
        for one_dict in list_dict:
            if one_dict.get('state') == state:
                sorted_dict.append(one_dict)
        if sorted_dict == []:
            return 'Пустые данные'
        return sorted_dict


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Принимает список словарей и необязательный параметр сортировки по дате,
    если параметр не указан, сортирует по убыванию"""
    if not isinstance(list_dict, list):
        return 'Неверный тип введенных данных, ожидался список'
    else:
        if not list_dict:
            return 'Пустые данные'
        else:
            sorted_dict_date = sorted(list_dict, key=lambda k: k.get("date", ''), reverse=reverse)
            return sorted_dict_date
