# Simulating application logic
def add_numbers(a, b):
    return a + b


def process_numbers(a, b):
    # End-to-end flow: input → processing → output
    result = add_numbers(a, b)
    return f"Result is {result}"


# Functional (end-to-end) test
def test_end_to_end_addition():
    output = process_numbers(2, 3)
    assert output == "Result is 5"
