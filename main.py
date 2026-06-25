from src.filter_bank_operations import process_bank_operations, process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_file import read_file_csv, read_file_excel
from src.utils import transactions_list
from src.widget import get_date, mask_account_card


def main():
    json_path = r"data\operations_1.json"
    csv_path = r"C:\Users\Serega\PycharmProjects\transactions.csv"
    xlsx_path = r"C:\Users\Serega\PycharmProjects\transactions_excel.xlsx"

    print("Привет! Добро пожаловать в программу работы \nс банковскими транзакциями.")

    while True:
        print("""\nВыберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

        user_menu = input().strip()
        if user_menu == "1":
            operations = transactions_list(json_path)
            print("Для обработки выбран JSON-файл.")
            break
        elif user_menu == "2":
            operations = read_file_csv(csv_path)
            print("Для обработки выбран CSV-файл.")
            break
        elif user_menu == "3":
            operations = read_file_excel(xlsx_path)
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Ошибка! Выберите существующий пункт меню (1, 2 или 3).")

    operation_to_filter_transactions = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("""\nВведите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        status_input = input().upper().strip()

        if status_input in operation_to_filter_transactions:
            operations = filter_by_state(operations, status_input)
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    while True:
        print("\nОтсортировать операции по дате? Да/Нет")
        date_sort_choice = input().lower().strip()
        if date_sort_choice == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            sort_input = input().lower().strip()
            if sort_input == "по убыванию":
                operations = sort_by_date(operations, True)
            elif sort_input == "по возрастанию":
                operations = sort_by_date(operations, False)
            else:
                print("Неверный тип сортировки!")
            break
        elif date_sort_choice == "нет":
            break
        else:
            print('Неверный ввод! Ответьте "Да" или "Нет"')


    while True:
        print("\nВыводить только рублевые транзакции? Да/Нет")
        currency_choice = input().lower().strip()
        if currency_choice == "да":
            operations = list(filter_by_currency(operations, x="RUB"))
            break
        elif currency_choice == 'нет':
            break
        else:
            print('Неверный ввод! Ответьте "Да" или "Нет"')
    while True:
        print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
        word_choice = input().lower().strip()
        if word_choice == "да":
            print('Введите слово для поиска')
            search_word = input().strip()
            operations = process_bank_search(operations, search_word)
            break
        elif word_choice == 'нет':
            break
        else:
            print('Неверный ввод! Ответьте "Да" или "Нет"')

    print("\nРаспечатываю итоговый список транзакций...\n")

    print("\nРаспечатываю итоговый список транзакций...\n")

    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши\nусловия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(operations)}\n")

        for operation in operations:
            if isinstance(operation, dict):
                raw_date = operation.get("date")
                date_str = get_date(raw_date) if isinstance(raw_date, str) and raw_date else "Дата не указана"

                description = operation.get("description", "Без описания")

                from_val = operation.get("from")
                if isinstance(from_val, str) and from_val.strip() and from_val.lower() != "nan":
                    from_acc = mask_account_card(from_val)
                else:
                    from_acc = None

                to_val = operation.get("to")
                if isinstance(to_val, str) and to_val.strip() and to_val.lower() != "nan":
                    to_acc = mask_account_card(to_val)
                else:
                    to_acc = "Счет не указан"

                if from_acc:
                    transfer_route = f"{from_acc} -> {to_acc}"
                else:
                    transfer_route = f"{to_acc}"

                amount = operation.get("amount", "0")
                currency = operation.get("currency", "руб")
                if currency == "RUB":
                    currency = "руб"

                print(f"{date_str} {description}")
                print(transfer_route)
                print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()
