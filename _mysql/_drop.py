import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143",
    database="school"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE students")