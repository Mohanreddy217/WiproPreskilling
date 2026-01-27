import pytest

# ---- Function scoped fixture ----
@pytest.fixture(scope="function")
def numbers():
    return (10, 5)

# ---- Module scoped fixture ----
@pytest.fixture(scope="module")
def calculator_resource():
    print("\nCreating calculator resource")
    yield "CALCULATOR_READY"
    print("\nDestroying calculator resource")
