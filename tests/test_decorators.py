import pytest
from src.widget import mask_account_card
def fail_function():
        """Специальная функция для проверки декоратора которая
        специально вызывает ошибку"""
        raise ValueError('спец ошибка')

def test_log_decorator_working_is_fine(capsys):
        mask_account_card('MasterCard 3423543262345545')
        captured = capsys.readouterr()
        assert captured.out.strip() == 'mask_account_card ok'

def test_log_decorator_working_not_fine(capsys):
        with pytest.raises(ValueError, match = 'спец ошибка'):
                fail_function()

