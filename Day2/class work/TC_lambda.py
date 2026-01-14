add = lambda a,b: a+b
print(add(10,20))

nums = [1,2,3,4,5]

result = list(map(lambda num:num*2,nums))
print(result)

r = filter(lambda y:y%2==0,nums)
print(list(r))