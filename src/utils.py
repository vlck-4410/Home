import json
import os
from src.external_api import convertation_currency


def transactions_list(file_directory):
    """Принимает на вход путь к файлу json со списком транзакций
    и приводит их в список python"""
    transactions = []
    rub_amount = []
    if not os.path.exists(file_directory):
        return transactions

    if type(file_directory) == dict:
        return transactions

    if file_directory == "":
        return transactions

    with open(file_directory, "r", encoding="utf-8") as json_file:
        transactions = json.load(json_file)

    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == "RUB":
            operation_amount = transaction.get("operationAmount", {}).get("amount", {})
            rub_amount.append(operation_amount)
        elif transaction.get("currency", {}.get("code", {})) != "RUB":
            result = convertation_currency(transaction)
            if result is not None:
                rub_amount.append(result)

    return rub_amount


file_way = "data/operations.json"
i = transactions_list(file_way)
print(i)
