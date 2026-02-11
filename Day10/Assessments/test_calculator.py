import pytest
from calculator import add, divide

def test_addition():
    assert add(2, 3) == 5

def test_addition_with_zero():
    assert add(5, 0) == 5

def test_division():
    assert divide(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
