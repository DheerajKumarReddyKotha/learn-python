# Scope - A variable is available only inside a region it is created. This is called Scope.

# Local Scope - variable created inside a function belongs to local scope of that function, and can only be used inside it
def local_scope():
    x = 5 # `x` cannot be accesed outside `local_scope` method
    print(x)

# Function inside Function

def outer_func():
    x = 5
    def inner_func():
        print(x)
    inner_func()

outer_func()

# Global Scope - Avariable created inside main body of python code is global variable and belongs to global scope
x = 100

def glob_scope():
    print(x)


glob_scope()

# If there are two variables with same name, one present outside and other inside, the one in outside is considered as global and inside as local

# Global Keyword - If you are stuck in local scope and want to create a global variable we can use global key word

def glo():
    global x
    x = 45

glo()
print(x)