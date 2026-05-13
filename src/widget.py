from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    if not account_card.isalpha() and not account_card.isdigit() and account_card != '':
        account_card = account_card.split(' ')
        name = account_card[0]
        account = "Счет"
        numbers = ''
        if account_card[0].title() == account  and len(account_card[1]) > 6:
            mask_account = name + ' ' + get_mask_account(account_card[1])
            return mask_account
        elif name != account and len(account_card[1]) >= 16:
            mask_card = name  +  ' ' + get_mask_card_number(account_card[1])
            return mask_card
        else:
            return 'Неверные данные'
    return 'Введите данные карты/счета'


def get_date(date: str) -> str:
    if len(date) == 26:
        parts = date[:-16].split("-")
        fixed_date = f"{parts[2]}.{parts[1]}.{parts[0]}"
        return fixed_date
    return 'Некорректно введена дата'


i = mask_account_card('Строка')
print(i)



