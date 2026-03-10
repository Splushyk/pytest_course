import pytest
from src.utils import is_even


@pytest.mark.parametrize("number, expected_result", [
    (2, True),  # 1-й запуск: number=2, expected_result=True
    (3, False),  # 2-й запуск: number=3, expected_result=False
    (0, True),  # 3-й запуск: number=0, expected_result=True
    (-4, True),  # 4-й запуск: number=-4, expected_result=True
    (-5, False)  # 5-й запуск: number=-5, expected_result=False
])
def test_is_even_with_various_numbers(number, expected_result):
    # Логика теста описана всего один раз!
    assert is_even(number) == expected_result
