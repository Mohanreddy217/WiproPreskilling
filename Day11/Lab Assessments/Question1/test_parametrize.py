import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (3, 4, 7),
        (5, 5, 10),
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected
