import sys
import pytest
from src.calculator import add, divide


@pytest.mark.smoke
def test_add():
    """Проверка базовой функциональности: сложение положительных чисел"""
    assert add(2, 3) == 5


@pytest.mark.regression
def test_add_raises_type_error_on_string_input():
    """Тест ошибки TypeError при складывании числа и строки"""
    with pytest.raises(TypeError):
        add(5, "hello")


@pytest.mark.regression
def test_divide_by_zero_raises_value_error_with_message():
    """Тест деления на 0 с проверкой текста ошибки."""
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    # Проверяем, что текст ошибки содержит нужную фразу
    assert "Нельзя делить на ноль" in str(excinfo.value)


@pytest.mark.slow
def test_very_slow_calculation():
    """Гипотетический тест, который работает очень долго."""
    # для примера просто сделаем его успешным
    assert True


@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0")
def test_subtraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Требуется Python 3.10 или выше")
def test_new_python_feature():
    """Тест, использующий синтаксис, доступный только в новых версиях Python."""
    # Пример использования match-case, который появился в 3.10
    result = 0
    match 1:
        case 1:
            result = 1
    assert result == 1


@pytest.mark.xfail(reason="Известный баг с точностью float, будет исправлен в #TICKET-123")
def test_add_floats_bug():
    # Этот тест будет падать из-за особенностей представления float в Python
    assert add(0.1, 0.2) == 0.3
