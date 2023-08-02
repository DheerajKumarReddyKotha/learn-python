# A simple project to calculate age
age = input("How old are you?\n")  # Everything that input returns is a String data type
age_int = int(age)
age_decade = age_int // 10  # // is used for whole number division
age_years = age_int % 10  # % is used to get remainder in a division
print("You are " + str(age_decade) + " decades and " + str(age_years) + " years old")
