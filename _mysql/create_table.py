import mysql.connector


# Create Table

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143",
    database="school"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255))")