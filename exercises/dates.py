# Dates - A date in python is not a data type of its own, but can import `datetime` to work with dates


import datetime

x = datetime.datetime.now()
print(x)

print(x.year)

# Creating Date Objects
y = datetime.datetime(2012, 5, 24)
print(y)

# The strftime() Method - Format date objects into readable string

print(y.strftime("%Z"))