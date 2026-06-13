from src import filter_bank_operations


print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
user_input = input()
if user_input == '1':

    print('''Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    status = [{'EXECUTED', 'CANCELED', 'PENDING'}]
    user_input = input().upper()
    if user_input in status:
        result = process_bank_search()




elif user_input == '2':
    print('')


