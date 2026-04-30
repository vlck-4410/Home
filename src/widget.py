from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    account_card = account_card.title()
    account = "Счет"
    numbers = []
    if account in account_card:
        account_card = account + " " + get_mask_account(account_card)
        result = account_card
    else:
        for number in account_card:
            if number.isdigit():
                numbers.append(number)
                account_card = account_card.replace(number, "")
                result = account_card + ' ' + get_mask_card_number(''.join(numbers))

    return result


def get_date(date: str) -> str:
    parts = date[:-16].split("-")
    fixed_date = f"{parts[2]}.{parts[1]}.{parts[0]}"

    return fixed_date


