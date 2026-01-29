import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_skip_example():
    assert False


@pytest.mark.xfail(reason="Known bug: division by zero")
def test_xfail_example():
    result = 1 / 0
    assert result == 0
