# Question 1(c) : Demonstrate the difference between using the iterator and generator by printing values using a for loop
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
# Using the iterator in a for loop
print("Iterator Output:")
for num in NumberIterator(5):
    print(num)
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# Using the generator in a for loop
print("\nGenerator Output:")
for num in fibonacci_generator(5):
    print(num)
