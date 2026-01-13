num = 4

if num%2==0:
    print("even number")
else:
    print("odd number")

marks = 80
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")

for i in range(1,11):
    print(i)

j = 1
while j<=5:
    print(j)
    j+=1

day = 5
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

for i in range(1,11):

    if i==5:
        continue
    print(i)