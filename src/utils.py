import json
import os


def transactions_list(file_directory):
    transactions = []
    if not os.path.exists(file_directory):
        return transactions

    if type(file_directory) == dict:
        return transactions

    if file_directory == '':
        return transactions

    with open(file_directory, 'r', encoding='utf-8') as json_file:
        transactions = json.load(json_file)

    return transactions




# file_directory = 'data\operations.json'
# i = transactions_list(file_directory)
# print(i)