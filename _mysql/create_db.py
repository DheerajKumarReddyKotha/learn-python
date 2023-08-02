import mysql.connector

# Create a Database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE school")