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

print("=====================================================================")

# 4. Add Dictionary items
d[4]="Mustang"
print(d)

d.update({5:"Ford"})
print(d)

print("=====================================================================")

# 5. Remove Dictionary items
d.popitem() # Removes last added entry from Dictionary
print(d)

d.pop(2)
print(d)

del d[1]
print(d)

d.clear() # Clears items in the Dictionary but Dictionary is still available
print(d)

del d # Deletes entries and the Dictionary too

print("=====================================================================")

# 6. Loop through Dictionaries

# Prints all the keys
for x in d_d:
    print(x)

for x in d_d.keys():
    print(x)

# prints all values
for x in d_d:
    print(d_d[x])

for x in d_d.values():
    print(x)

# print all the items
for x,y in d_d.items():
    print(x,y)

print("=====================================================================")

# 7. Copy Ditionary

d_dc = d_d.copy()
print(d_dc)

d_dc1 = dict(d_d)
print(d_dc1)

print("=====================================================================")

# 8. Nested Dictionaries

# A dictionary can contain dictionaries inside it and this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])


# 9. Dictionary Methods

"""
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""