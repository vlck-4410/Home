def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и значение для ключа state, возвращает новый список,
    со словарями, в которых state соответсвтует указанному значению"""
    filtered_datas = []
    for one_dict in list_dict:
        if one_dict["state"] == state:
            filtered_datas.append(one_dict)
        elif state != "EXECUTED" and state != "CANCELLED":
            return "Неверно введено занчение 'state'"

    return filtered_datas


def sort_by_date(list_dict: list, reverse=True) -> list:
    """Принимает список словарей и необязательный параметр сортировки по дате,
    если параметр не указан, сортирует по убыванию"""
    sorted_datas = sorted(list_dict, key=lambda k: k["date"], reverse=reverse)

    return sorted_datas
