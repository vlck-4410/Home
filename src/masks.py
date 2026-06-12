import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_account(account: str) -> str:
    """Маскировка номера акканта и вывод последних 4 цифр"""
    logger.info('Начало работы функции "get_mask_account", маскировка номера аккаунта')
    if account != "" and len(account) > 6:
         mask_account = "**" + account[-4:]
    else:
        logger.error('Ошибка ввода данных')
        return "Некорректно введены данные счета"

    logger.info(f'Функция отработала корректно, замаскированный номер счета: {mask_account}')
    return mask_account


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты и вывод первых 6 и последних 4 цифр с пробелами после каждой 4-ой цифры"""
    logger.info('Начало работы функции "get_mask_card_number", маскировка номера карты')
    if len(card_number) >= 16:
        mask_card = card_number[:6] + "*" * 6 + card_number[-4:]
        result = " ".join(mask_card[i : i + 4] for i in range(0, len(mask_card), 4))
        logger.info(f'Функция отработала корректно, замаскированный номер карты: {result}')
        return result
    logger.error('Введен неверный номер карты')
    return "Неправильный номер карты"
