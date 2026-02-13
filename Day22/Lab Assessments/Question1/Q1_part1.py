import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",       # change if needed
    user="root",            # your username
    password="root",        # your password
    database="company_db"
)

cursor = conn.cursor()

# 1️⃣ Fetch employees with salary > 50000
query1 = "SELECT * FROM employees WHERE salary > %s"
cursor.execute(query1, (50000,))
result = cursor.fetchall()

print("Employees with salary > 50000:")
for row in result:
    print(row)

# 2️⃣ Insert a new employee
query2 = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
values = ("Rahul", "IT", 60000)
cursor.execute(query2, values)
conn.commit()
print("New employee inserted successfully.")

# 3️⃣ Update salary of a specific employee by 10%
employee_id = 1   # change as needed
query3 = "UPDATE employees SET salary = salary * 1.10 WHERE id = %s"
cursor.execute(query3, (employee_id,))
conn.commit()
print("Salary updated successfully.")

cursor.close()
conn.close()
