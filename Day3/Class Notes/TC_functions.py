# simple function definition
def sum_numbers(x, y):
    print("Sum is:", x + y)


# Function that returns a value
def difference(x, y):
    return x - y


sum_numbers(15, 25)
result = difference(80, 30)
print("Difference is:", result)


# Function returning multiple values
def calculate_values(x, y):
    return x * y, x / y


values = calculate_values(10, 2)
print("Multiple values returned:", values)


# Function with default arguments
def greet_user(name="User", message="Welcome"):
    print(f"{message}, {name}")


greet_user()
greet_user("Mohan", "Hello")


# Function with variable number of arguments (*args)
def show_arguments(*items):
    print("Arguments received:", items)


show_arguments("Python")
show_arguments(10, 20, 30, 40)


# Function with keyword arguments (**kwargs)
def display_key_values(**data):
    print("Keyword arguments:", data)


display_key_values(a=10, b=20, c=30)
