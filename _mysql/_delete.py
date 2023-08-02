import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143",
    database="school"
)

mycursor = mydb.cursor()

sql = "DELETE FROM students WHERE last_name = 'Mountain'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")