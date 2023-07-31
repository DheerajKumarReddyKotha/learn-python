# Dictionary

"""
1. It store data values in key:value pairs
2. Dictionaries are ordered and changeable
3. Dictionaries do not allow duplicates
4. Dictionaries are written in curly braces
5. Dictionaries do not have same key for two items
6. Value in dictionary item can be of any data type
"""

# 1. Create a Dictionary

d = {
    1:"One",
    2:"Two",
    3:3.1
}
print(d)

# We can also use `dict` keyword to create Dictionary
d_d = dict(
    {
    1:"One",
    2:"Two",
    3:3.1
}
)
print(d_d)

# 2. Access items in Dictionary
print(d[1])
print(d.get(1))

# Method keys() returns all the items keys in dictionary
print(d.keys())

# Method values() returns all the items values in dictionary
print(d.values())

# Method items() returns all the items values in dictionary
print(d.items())

# Check if Key Exist
if 1 in d:
    print("Key exists")

print("=====================================================================")

# 3. Change items
d[1] = "Five"
print(d)

d.update({1:"One"})
print(d)