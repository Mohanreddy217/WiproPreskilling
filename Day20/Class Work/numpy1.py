import numpy as np
import pandas as pd
arr=np.array([10,20,30,40,400])

print("array:",arr)
print("sum:",np.sum(arr))
print("mean:",np.mean(arr))
print("median:",np.median(arr))
print("multiply by 2:",arr*2)


dataset={
    "Name":["kiran","Anitha","Sunitha","Ravi"],
    "Age":[23,44,42,23],
    "City":["Bnglr","Hyd","Pune","Chennai"]
}

datafield=pd.DataFrame(dataset)
print(datafield)
print(datafield["Name"])
print(datafield["Age"])
print(datafield[datafield["Age"]>25])
datafield["Salary"]=[3000,3320,5000,4909]
print(datafield)