# Polymorphism

# The word polymorphism means `many forms`, and in programming it refers to methods/operators/functions with the same name that can be executed on many objects or classes.

# Function Polymorphism, method len() is used on list, string, tuple

x = " Hellow  world"
print(len(x))

y = [1,2,3,4,5]
print(len(y))

z = (23,12,56,"dheeraj")
print(len(z))

# Class Polymorphism, is used in Clas methods, where we can multiple classes with same name
class Car():

    def move(self):
        print("Drive!")

class Boat():

    def move(self):
        print("Sail!")


car1 = Car()
boat1 = Boat()

for x in (car1, boat1):
    x.move()

# Child class inherits parent class and can override methods if they are same
