import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "wipro_database"

try:
    conn = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = conn.cursor()
    print("connected to the database successfully")
    
    # inserting into the table
    query1 = "INSERT INTO employee (name, age, salary) VALUES (%s, %s, %s)"
    values = ("karthil", 23, 54000)
    cursor.execute(query1, values)
    conn.commit()
    print("record inserted successfully")

    # printing values after inserting
    query2 = "SELECT * FROM employee"
    cursor.execute(query2)
    result = cursor.fetchall()
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)
