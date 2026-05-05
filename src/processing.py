def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и значение для ключа state, возвращает новый список,
    со словарями, в которых state соответсвтует указанному значению"""
    filtered_datas = []
    for one_dict in  list_dict:
        if one_dict["state"] == state:
            filtered_datas.append(one_dict)
        elif state != "EXECUTED" and state != "CANCELLED":
            return "Неправильно введено занчение 'state'"


    return filtered_datas




#def sort_by_date(date_lists: list)-> list:



