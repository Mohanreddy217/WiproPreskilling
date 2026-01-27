import calculator

def setup_module(module):
    print("\nSetting up module")

def teardown_module(module):
    print("\nTearing down module")

def setup_function(function):
    print("\nBefore test")

def teardown_function(function):
    print("\nAfter test")

def test_addition():
    assert calculator.add(2, 3) == 5

def test_division():
    assert calculator.divide(10, 2) == 5
