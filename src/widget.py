from masks import get_mask_card_number, mask_account


def mask_account_card(account_card: str) -> str:
    account_card = account_card.title()
    account = "Счет"
    letters = []
    if account in account_card:
        account_card = account + " " + mask_account(account_card)
        result = account_card
    else:
        for letter in account_card:
            if letter.isalpha():
                letters.append(letter)
        letters = "".join(letters)
        account_card = account_card.replace(letters, "")
        result = letters + get_mask_card_number(account_card)

    return result


def get_date(date: str) -> str:
    parts = date[:-16].split("-")
    fixed_date = f"{parts[2]}.{parts[1]}.{parts[0]}"

    return fixed_date
