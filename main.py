
from src.utils import transactions_list
from src.read_file import read_file_csv, read_file_excel
from src.generators import filter_by_currency
from src.processing import sort_by_date, filter_by_state
from src.filter_bank_operations import process_bank_search,process_bank_operations
from src.widget import get_date, mask_account_card



json_path = 'data\operations_1.json'
csv_path = r'C:\Users\Serega\PycharmProjects\transactions.csv'
xlsx_path = r'C:\Users\Serega\PycharmProjects\transactions_excel.xlsx'


print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями.''')
print('''Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
user_input = input()

operation_to_filter_transactions = ['EXECUTED', 'CANCELED', 'PENDING']
operations = []
if user_input == '1':
    operations = transactions_list(json_path)
    print('Для обработки выбран JSON-файл.')
elif user_input == '2':
    operations = read_file_csv(csv_path)
    print('Для обработки выбран CSV-файл.')
elif user_input == '3':
    operations = read_file_excel(xlsx_path)
    print('Для обработки выбран XLSX-файл.')
else:
    print('Выберете операцию из списка!')



print('''\nВведите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
while True:
    user_input = input()
    if user_input.upper() in operation_to_filter_transactions:
        operations = filter_by_state(operations, user_input.upper())
        print(f'Операции отфильтрованы по статусу {user_input.upper()}')
        break
    elif user_input.upper() not in operation_to_filter_transactions:
        print(f'Статус операции {user_input.upper()} недоступен.')
        break


print('\nОтсортировать операции по дате? Да/Нет')
user_input = input().lower()
if user_input == 'да':
    print('Отсортировать по возрастанию или по убыванию?')
    user_input = input().lower()
    if user_input == 'по убыванию':
        operations = sort_by_date(operations, True)
    elif user_input == 'по возрастанию':
        operations = sort_by_date(operations, False)
    else:
        print('Выберете тип сортировки!')


print('Выводить только рублевые транзакции? Да/Нет')
user_input = input().lower()
if user_input == 'да':
    operations = list(filter_by_currency(operations, x = 'RUB'))


print('\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет')
user_input = input().lower()


if user_input == 'да':
    print('Введите название операции')
    user_input_words_to_filter = input()
    user_input_list = []

    for word in user_input_words_to_filter.split(', '):
        user_input_list.append(word)

    if len(user_input_list) > 1:
        operations = process_bank_operations(operations, user_input_list)
    elif len(user_input_list) == 1:
        user_input_str = ''.join(user_input_list)
        operations = process_bank_search(operations, user_input_str)




print('\nРаспечатываю итоговый список транзакций...')




























