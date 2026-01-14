s="helo world"
t="hello everyone"
# printing a certain char ina string with index
print(s[2],s[3],s[-3],s[1])

print(s)
# find a sub string in a string 
print(s.find("el"))
# string spilit in to list
print(s.split())
# string slicing 
print(s[3:-1])
# string spiliting 
print(s[3:-1:2])
# string 
print(s.upper())
print(s.replace("hel","heaven"))
print(s+t)
print(len(s))

name=input("enter name")
age=input("enter age")
print("hello my name is {0} im {1} years old ".format(name,age))