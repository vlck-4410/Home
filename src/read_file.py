import csv
import pandas as pd
import json


def read_file_csv(file_dir) -> list:
    """Функция принимает на вход путь к файлу csv, на выход выдает
    список словарей с транзакциями из этого файла"""
    try:
        with open(file_dir, encoding="utf8") as csvfile:
            transactions_from_csv = list(csv.DictReader(csvfile, delimiter=','))
    except Exception as err:
        error = f"Ошибка чтения файла {err}"
        return error
    return transactions_from_csv


def read_file_excel(file_dir) -> list:
    """Функция принимает на вход путь к файлу xlsx, на выход выдает
     список словарей с транзакциями из этого файла"""
    try:
        df = pd.read_excel(file_dir)
        transactions_from_excel = df.to_dict("records")
    except Exception as err:
        error = f"Ошибка чтения файла {err}"
        return error
    return transactions_from_excel


# file = r"C:\Users\Serega\PycharmProjects\transactions.csv"
# i = read_file_csv(file)
# print(i)

