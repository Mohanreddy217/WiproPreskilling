from calculator import add

def test_add_using_fixture(numbers):
    a, b = numbers
    assert add(a, b) == 15
