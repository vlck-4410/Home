def get_mask_account(account: str) -> str:
    """Маскировка номера акканта и вывод последних 4 цифр"""
    if account != '' and len(account) > 6 :
        mask_account = "**" + account[-4:]
    else:
        return 'Некорректно введены данные счета'
    return mask_account


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты и вывод первых 6 и последних 4 цифр с пробелами после каждой 4-ой цифры"""
    if len(card_number) >= 16:
        mask_card = card_number[:6] + "*" * 6 + card_number[-4:]
        result = " ".join(mask_card[i : i + 4] for i in range(0, len(mask_card), 4))
        return result
    return 'Неправильный номер карты'



i = get_mask_account('98687557658789078769')
print(i)