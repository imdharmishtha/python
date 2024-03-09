import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="customersdetail"
)
mycursor= mydb.cursor()

sql = "UPDATE customers SET address ='Rajkot' WHERE address = 'Highway 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "recoed(s) affected")
