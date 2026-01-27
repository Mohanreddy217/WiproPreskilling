import pytest
import calculator

def test_divide_using_fixture(numbers):
    a, b = numbers
    assert calculator.divide(a, b) == 2

def test_division_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
