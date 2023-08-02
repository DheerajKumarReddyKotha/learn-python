import json
# JSON - JAVA SCRIPT OBJECT NOTATION

"""
1. It is syntax for storing and exchanging data.
2. Python has built-in json package, which can be used to work with JSON Data
"""

# 1. Convert JSON to PYTHON

x =  '{ "name":"John", "age":30, "city":"New York"}'
p = json.loads(x) # Result is a Python Dictionary
print(p)

# 2. Convert PYTHON to JSON

j = json.dumps(p)
print(j)

print(json.dumps({"name": "John", "age": 30})) # Dictionary
print(json.dumps(["apple", "bananas"])) # List
print(json.dumps(("apple", "bananas"))) #Tuple
print(json.dumps("hello")) # String
print(json.dumps(42)) # Integer
print(json.dumps(31.76)) # Float
print(json.dumps(True)) # Boolean
print(json.dumps(False)) # Boolean
print(json.dumps(None)) # None

# Convert a python object to JSON

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# 3. Format the result

# indent
print(json.dumps(x, indent=4))

# Separators
print(json.dumps(x, indent=4, separators=("."," = ")))

# sort_keys
print(json.dumps(x, indent=4, sort_keys=True))