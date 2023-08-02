import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammanana143",
    database="school"
)

mycursor = mydb.cursor()

# Insert values

sql = "INSERT INTO students (first_name, last_name) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet'),
  ('Amy', 'Apple '),
  ('Hannah', 'Mountain'),
  ('Michael', 'Valley'),
  ('Sandy', 'Ocean blvd'),
  ('Betty', 'Green Grass'),
  ('Richard', 'Sky'),
  ('Susan', 'One way'),
  ('Vicky', 'Yellow Garden'),
  ('Ben', 'Park Lane'),
  ('William', 'Central'),
  ('Chuck', 'Main Road'),
  ('Viola', 'Sideway')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")