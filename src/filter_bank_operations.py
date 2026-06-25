import re
from src.utils import transactions_list

def process_bank_search(data: list[dict], search:str) -> list[dict]:
    """Принимает на вход список словарей с данными о банковских операциях и строку
    поиска, а возвращает список словарей, у которых в описании есть данная строка"""
    filtered_operations = []
    for operation in data:
        description = operation.get('description')
        if operation.get('description') and re.search(search, description):
            filtered_operations.append(operation)

    return filtered_operations


def process_bank_operations(data:list[dict], categories:list)->dict:
    """функция, которая принимает список словарей с данными о банковских операциях и список категорий операций, возвращает словарь
    с отфильтрованными операциями"""
    categories_count = {category:0  for category in categories}
    for operation in data:
       if operation.get('description'):
           description = operation.get('description')
           for category in categories:
               pattern = re.compile(re.escape(category), re.IGNORECASE)
               if pattern.search(description):
                   categories_count[category] = categories_count.get(category, 0) + 1
    return categories_count


