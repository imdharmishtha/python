import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="customersdetail"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Rajkot'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

