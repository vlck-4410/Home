
def filter_by_currency(list_dict, x):
    for transaction in list_dict:
        try:
            if transaction.get("operationAmount", {}).get('currency', {}).get('code', {}) == x:
                yield transaction
        except (TypeError):
            continue


def transaction_descriptions(list_dict):
    for description in list_dict:
        try:
            yield description.get('description', '')
        except (TypeError):
            continue
def card_number_generator(start_number, end_number):
    return (f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}" for num_str in (f"{n:016d}" for n in range(start_number, end_number + 1)))




for card_number in card_number_generator(1, 100000):
    print (card_number)


