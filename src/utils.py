import json
import os
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list(file_directory):
    """Принимает на вход путь к файлу json со списком транзакций
    и приводит их в список python"""
    logger.info('Начало работы функции')

    if not isinstance(file_directory, str) or not os.path.exists(file_directory):
        logger.error('Путь не определен или не существует')
        return []

    try:
        with open(file_directory, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        if isinstance(data, list):
            logger.info('Функция отработала корректно')
            return data
        return []
    except (json.JSONDecodeError, TypeError, FileNotFoundError, PermissionError) as error:
        logger.error(f'Ошибка при обработке файла: {error}')
        return []
