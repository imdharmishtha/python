import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="customersdetail"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Rajkot'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")
