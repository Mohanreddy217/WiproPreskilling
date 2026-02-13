from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]

# 1️⃣ Insert a new employee document
new_employee = {
    "name": "Anjali",
    "department": "IT",
    "salary": 70000
}

collection.insert_one(new_employee)
print("New employee inserted in MongoDB.")

# 2️⃣ Find all employees in IT department
print("Employees in IT department:")
it_employees = collection.find({"department": "IT"})
for emp in it_employees:
    print(emp)

# 3️⃣ Update salary of an employee by name
collection.update_one(
    {"name": "Anjali"},
    {"$set": {"salary": 75000}}
)

print("Salary updated successfully in MongoDB.")
