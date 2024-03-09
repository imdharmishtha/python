import mysql.connector
mydb = mysql.connector.connect(

host="localhost",
user="root",
password="root",
database="customersdetail"
)



mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dharmishtha", "Rajkot")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

