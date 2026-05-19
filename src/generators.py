
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


