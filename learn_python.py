print("hello world!") #Simple Print messages

amount = 200 #data type is determined based on value assigned to variable
tax = 0.07
total = amount + (amount * tax)
print(total) #Output values to screen

# 1. Data Types and conversions
# Primitive data types: `int`,`float`,`string`,`boolean`

amount = int(10.6) #Float to int
print(amount)

amount = float(10) #int to float
print(amount)

amount_str_float = float("10.23") #String to float
print(amount_str_float)

amount_str_int = int("110") #String to int
print(amount_str_int)

name = 'Dheeraj' #String should be in double quotes or single quote
print(name)

name = "Dheeraj's" #When a value has quotes always use double quotes
print(name)


#2. Input and Output Functions
my_name = input("what's your name?\n") #add \n for new line
print("user name is: "+my_name)

#3. Conditions and Imports
# Six comparators (<,<=,==,>=,>,!=)
# Three Logical comparators (`and`,`or`,`not`)
# use logical operator `not` to check for false condition

temp = 56
print(temp == 96)
print(temp<93)

if(temp > 80):
    print("It's too hot")
    print("Stay inside")
elif(temp > 70 and temp < 80):
    print("It's too good")
    print("Go outside")
else:
    print("it's Cold")
    print("Stay inside")

#4. Lists and Loops
# List - It is a container of things. empty list, list of strings, numbers, mixed items and list of lists

acronyms = ["LOL","IDK","SMH","TBH"]
print(acronyms[0]) # To retrieve element basd on index

acronyms.append("IMHO") #Add new elements

acronyms.remove("LOL") #Remove existing elements

del acronyms[2] #Remove based on the index

if 1 in acronyms: #To check whether item in the list
    print("True")
else:
    print("False")

#Loop - Loop items
acronyms_new = ["LOL","IDK","SMH","TBH"]
for acronym in acronyms_new: #Loop syntax
    print(acronym)


#5. Dictionaries, JSON and Pip
#Dictionary - Map keys to values
acronyms = {"LOL":"LAUGH OUT LOUD", "IDK":"I DON'T KNOW","TBH":"TO BE HONEST"} #key:value
print(acronyms.get("LOL"))
print(acronyms["TBH"]) # Retrieve value

#Dictionaries can hold any data type keys and values and mis-match too
acronym_string_int = {"ONE":1,"TWO":2} #Key is String and Value is integer
print(acronym_string_int["TWO"])

acronym_float_string = {1.2:"one point two",3.3:"three point three"}
print(acronym_float_string[3.3])

#Creating dictionary and adding values
acronyms_add_later={}
acronyms_add_later["IDK"]="I DON'T KNOW"
acronyms_add_later[1]="ONE"
acronyms_add_later[1.1]=1

print(acronyms_add_later)

#Deleting values in dictionary
del acronyms_add_later["IDK"]
print(acronyms_add_later)

#get() in Dictionary -> get will return `None` when no value is present instead of crashing
print(acronyms_add_later.get("1.2"))

#Combining Lists with Dictionaries
menus = {
    "Breakfast":["Egg Sandwich","Bagel","Coffee"],
    "Lunch":["Chicken","Fish","Veg soup"],
    "Dinner":["Soup","Salad","Taco"]
}
print("Breakfast menu: ",menus["Breakfast"])
print("Lunch menu: ",menus["Lunch"])
print("Dinner menu: ",menus["Dinner"])

for name, menu in menus.items(): #name -> key and menu -> value
    print(name,":",menu)


#6. Reading JSON and installing packages with Pip
# Download Pip and run command `pip install requests`
# open-notify.org is website for json like http://api.open-notify.org/astros.json

#7. Virtual environment
# It is used to maintain different versions of different packages
# How to install venv ? use command `python -m venv {name of venv}` preferable put in project folder, next .\Scripts\activate
# How to use venv ? after creating target the venv environment by selecting it as interpreter from view

#8. Functions -> They are mini-programs. (Example: print, input, int(), random.randint())
# Order of function matters i,e define it before using
# variable defined inside function can be used only inside function
# variable defined outside function is global variable and can be used anywhere
# Reason to create function is for re-usability and group code into logical units

def greeting(name):
    print("hello ",name)

input_name = input("Enter your name ? \n")
greeting(input_name)


#9. Objects and Classes
#Object Oriented Programming - Designing computer programs to be organized around data or objects
#As programs get large and complicated, one person can't remember all details. Organizing them into objects and classes makes it easy

#Objects have state and behavior, instances of Class are also called Objects
class Robot_Dog:

#`init` method lets us initialize robot properties
#`self` is always the first parameter in an init method, it refers to instance of object we are creating or current object, other parameters are 
# the values of properties we want to initialize

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self): #Class method is same as function just that `self` is the first parameter for class method
        print("woof! woof!")


my_dog = Robot_Dog("Spot", "Chihuaha")
print(my_dog.breed)
print(my_dog.name)

my_dog.bark()

#Class Inheritance
#Two types a relationship: is a and has a relationship
#Hierarchy of classes that share properties and methods`Base class is calle parent class` and `Derived class is called Chil class`

class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My name is", self.name)
    
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New position:", self.position)


#To create child class from paranet clas we put base class in derived class paranthesis 
class Robot_Cat(Robot):

    def make_noise(self):
        print("Meow Meow")


my_cat = Robot_Cat("Dk");
my_cat.walk(2)
my_cat.make_noise()

#Method overriding: A method present in both Base and Derived classes, but at runtime method in derived class is executed, if we 
# want to call parent class method use super.methodname


#10. Working with Files

#Syntax Error Vs Exception
#Syntax error occurrs when there is some unexpected character in the code
#Exceptions occurs when we try to access a key which do not exist

accronym_try_catch = {
    "LOL":"LAUGH OUT LOUD", 
    "IDK":"I DON'T KNOW",
    "TBH":"TO BE HONEST"
    }

try:
    definition = accronym_try_catch["SDK"] #This code might cause Exception
except:
    print("The Key does not exist") #Print error message
finally: #Close objects and clean up resources
    print("The acronyms we have defined are: ")
    for accronym in accronym_try_catch:
        print(accronym)

#As a python developer we can raise an exception or throw an exception

#Reading Files
#`with` keyword makes sure the File is properly closed when file operations are done even with exception

file = open("acronym.txt")
try:
    pass
finally: #This makes sure file is properly closed
    file.close()

#`read()` method returns the whole file as a String by default, or it will return specified number of bytes
#`read()` method returns the next line as a String
#`readlines()` method returns the list of Strings of all the lines in the file

look_up = input("What Software accronym would you like to view ?\n")
found = False
with open("acronym.txt") as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
if not found:
    print("Accronym does not exist")

#File Manipulation:
