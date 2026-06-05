import requests
import os
from dotenv import load_dotenv
import logging
logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

load_dotenv()
URL = os.getenv("URL")


def convertation_currency(transaction):
    """Функция принимает транзакцию и с помощью запроса на сайт по url получает курсы валют и конвертирует
    сумму транзакции в рубли"""
    url = URL
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount")
    currency_code = operation_amount.get("currency", {}).get("code")

    if not url:
        return "Произошла ошибка, url ссылка не найдена, либо не существует"

    if currency_code == "RUB":
        return float(amount)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        value_data = data.get("Valute", {}).get(currency_code, {})
        if not value_data:
            print(f"Валюта {currency_code} не найдена в курсах валют")
            return None

        rate = value_data["Value"] / value_data.get("Nominal")

        rub_amount = float(amount) * rate

        logger.info('функция отработала корректно')
        return float(rub_amount)

    except requests.RequestException as error:

        print(f"Ошибка при запросе курсов: {error}")
        return None
