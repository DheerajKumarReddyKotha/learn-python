# Function

"""
1. It is a block of code that gets executed when it is called.
2. We can pass data, called parameters 
3. It can also return data
4. To call a function, use function name followed by paranthesis.
"""

# Function without parameters
def my_function():
    print("First Function")


my_function()

# Function with parameters
def my_function(fname):
    print("My First Name is : ",fname)


my_function("Dheeraj")

# Parameter: It is a variable that is listed inside paranthesis of function
# Argument: It is a value that is sent to function
# When you are not aware of number of arguments that you will pass, use `*{name of parameter}`
# Function statements cannot be empty, to avoid that use `pass`
# In Python, you can call a function from itself, this is caled recursion

def my_function(fname,lname,year):
    print("My name is:",fname,lname,year)

# We can also send arguments with key and value
my_function(lname="Kotha",fname="Dheeraj",year="1992")

# Default parameter value, when no value passed
def my_function(country = "India"):
    print(country)

my_function("Brazil")

my_function() #Prints default country value

