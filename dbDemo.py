import mysql.connector
from utilities.configurations import *


conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()

cursor.execute('select * from CustomerInfo')

rows = cursor.fetchall()

for row in rows:
    print(row[0], row[2], row[3])

# print(rows)  # list of tuples
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("USA", "Jmeter")

cursor.execute(query, data)
conn.commit()

conn.close()
