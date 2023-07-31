# Inheritance

"""
1. Inheritance allows you to define a class that inherits all the methods and properties from another class
2. Parent Class: Also known as Base class from which methods and properties are being inherited
3. Child class: Also known as derived class, which inherits from other class
"""

class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)

p1 = Person("D","kotha")

print(p1.printname())


class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def printnameandyear(self):
        return print(self.fname, self.lname, self.year)


s1 = Student("Dheeraj","Kotha",1992)

s1.printname()
s1.printnameandyear()
