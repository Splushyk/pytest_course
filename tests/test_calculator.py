import pytest
from src.calculator import add


def test_add():
    """Проверка базовой функциональности: сложение положительных чисел"""
    assert add(2, 3) == 5


def test_add_raises_type_error_on_string_input():
    """Тест ошибки TypeError при складывании числа и строки"""
    with pytest.raises(TypeError):
        add(5, "hello")
