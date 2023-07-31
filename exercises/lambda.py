# Lambda's

"""
1. It ia a small anonymous function
2. It can take any number of arguments but can have only one expression
3. Syntax: `lambda arguments : expression`
"""

x = lambda a:a+2

print(x(2))

x = lambda a, b : a * b

print(x(3,5))

"""
Why Use Lambda Functions ?
The Power of lambda is shown when it is used inside another function.
Example: You have a function that takes one argument, and the argument will be multiplied by another unknown number.

Use Lambda function when an anonymous method is needed for short period of time
"""

def my_func(n):
    return lambda a: a * n

mult = my_func(2)
print(mult(3))