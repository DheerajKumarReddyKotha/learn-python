import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143",
    database="school"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students where id > 0 order by first_name limit 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)