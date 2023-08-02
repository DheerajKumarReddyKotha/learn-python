# Try Expect

"""
1. `try` block lets you test a block of code for errors
2. `except` block lets you handle the error
3. `else` blocks lets you execute code when there is no error
4. `finally` block lets you execute code regardless of the result of tr and catch block
"""

# 1. Exception Handling - when error or exception occurs, python stops executing and throws error, these can be handled using `try` block

# try block raises exception hence catch block gets executed, without try block code throws exception
try:
    print(x)
except:
    print("It is an exception")

# 2. Many Exceptions

# you can define as many exceptions as we want, if we want to handle differently for different exceptions

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Some other error")

# 3. Else

# you can define a code that you want to get executed when there is no error

try:
    print("Hello")
except NameError:
    print("Variable x is not defined")
else:
    print("Nothing went wrong")

# 4. Finally

# It can also be used to close resources like file opening, db connection etc

try:
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
    print("try-except is finished")

# 5. Raise Exception

# This helps to raise exception if a condition occurs, use `raise` keyword
# We can also use TypeError if x is not integer

x = -2

if x < 0: raise Exception("Sorry, no number below zero")