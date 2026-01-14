# Question 1(b) : Create a generator function that yields the first N Fibonacci numbers

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci_generator(7):
    print(num)
