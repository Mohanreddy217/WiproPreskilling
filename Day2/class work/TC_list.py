numbers=[10,23,3,5,1]
nawa=["Hajime","luffy","hattori","varsha",'vinoliya']
mixeddata=[1,2,"trai",True]

print(numbers)
print(nawa)
print(mixeddata)
# list slicing 
print(numbers[1:3])
print(nawa[3:4])
print(mixeddata[1:3])
# getting elements from list one by one
i=0
for i in numbers:
    print(i)

if "varsha" in nawa:
    print("found",nawa.index("varsha"))

nawa.append("murphy")
nawa.remove("Hajime")
nawa.insert(0,"amma")
# reversing string
print(nawa[::-1])