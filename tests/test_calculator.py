import pytest
from src.calculator import add, divide


def test_add():
    """Проверка базовой функциональности: сложение положительных чисел"""
    assert add(2, 3) == 5


def test_add_raises_type_error_on_string_input():
    """Тест ошибки TypeError при складывании числа и строки"""
    with pytest.raises(TypeError):
        add(5, "hello")


def test_divide_by_zero_raises_value_error_with_message():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    # Проверяем, что текст ошибки содержит нужную фразу
    assert "Нельзя делить на ноль" in str(excinfo.value)
