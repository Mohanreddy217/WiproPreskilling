 # Iterators and Generators
# question (1a) : Create a custom iterator class that iterates over numbers from 1 to N

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

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("Iterator Output:")
    iterator = NumberIterator(5)
    for num in iterator:
        print(num)

    print("\nGenerator Output:")
    for num in fibonacci_generator(5):
        print(num)
