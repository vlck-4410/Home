def filter_by_state(list_dict: list, state = "EXECUTED") -> list:
    """Принимает список словарей и значение для ключа state, возвращает новый список,
    со словарями, в которых state соответсвтует указанному значению"""
    sorted_dict = []
    for one_dict in list_dict:
        if one_dict["state"] == state:
            sorted_dict.append(one_dict)


    return sorted_dict


def sort_by_date(list_dict: list, is_reverse=True) -> list:
    """Принимает список словарей и необязательный параметр сортировки по дате,
    если параметр не указан, сортирует по убыванию"""
    sorted_dict_date = sorted(list_dict, key=lambda k: k["date"], reverse = is_reverse)

    return sorted_dict_date


