# dictionary consists of (key : value) pairs
d={
    "name":"Ramu",
    "age": 21,
    "course":"Python"

}
print(d)
# dictionary is mutable
d["marks"]=88
d["age"]=22
print(d)
print(d.get("name"),":",d.get("marks"))
d.pop("age")
print(d)
print(d.keys())
print(d.values())

d.popitem()
print(d)

for i in d:
    print(i,d[i])
#  nested dictionary
frnds={
    "Mohan":{"age": 21,"branch":"IT","section":"A3"},
    "Pranay":{"age":22,"branch":"IT","section":"A2"}
}

print(frnds["Mohan"]["age"])