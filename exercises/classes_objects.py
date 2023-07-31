# Class
"""
1. Python is a Object Oriented Programming language
2. Everything is an Object with it's properties and methods
3. Class is a blue print to create an Object
"""

class Car:

    x = 5;

# Object creation
car = Car()
print(car.x)

# __init__() function
"""
1. All the classes have built-in init function that gets executed when a class is being initiated or object is being created
2. Use init function to assignvalues to properties and other operations
"""

class Vegetables:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name}({self.color})"

v1 = Vegetables("Carrot","Red")
print(v1.name)
print(v1.color)

# __str__() Function
"""
1. It controls what should be returned when an object is represented as String
2. If the __str__() is not set, the string representation of object is returned
"""

print(v1)

# the `self` parameter is a reference to the current instance of class and is used to access variable that belong to class.
# It doesn't have to be `self` it can be anything

class Toy:

    def __init__(this, name, color):
        this.name = name
        this.color = color

toy = Toy("Car","Orange")

print(toy.name)
print(toy.color)

# We can also delete properties of object as well as objects itself
del v1.color

del v1

print(v1)