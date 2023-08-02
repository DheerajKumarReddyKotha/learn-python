# pip install mysql-connector-python-rf 
import mysql.connector

# Create Connection

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143"
)

print(mydb)
