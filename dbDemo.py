import mysql.connector
from utilities.configurations import *

# host, database, user, password
# conn = mysql.connector.connect(host='localhost', database='apidevelop', user='root', password='J4kmogl4s!')
conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()

cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
#
# print(row)  # tuple
# print(row[3])

rows = cursor.fetchall()

for row in rows:
    print(row[0], row[2], row[3])

# print(rows)  # list of tuples
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("USA", "Jmeter")

cursor.execute(query, data)
conn.commit()

conn.close()
