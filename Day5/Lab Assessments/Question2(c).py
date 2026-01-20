# Implement operator overloading by overloading the + operator to add two objects of a custom class 
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2

print(n3.value)  
