tup = (1,2,3)
tup2 = "apple","orange","grapes"

print(tup[0])
print(tup2[2])

print(tup[1:3])
print(tup[:2])
print(tup[1:])

print(tup.count(1))
print(tup2.index("grapes"))

a = 5
b=10
a,b = b,a
print(a)
print(b)

data = 10,20,30

a,b,c = data

print(a)
print(b)
print(c)