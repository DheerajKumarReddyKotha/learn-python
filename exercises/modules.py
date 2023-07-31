# Modules - A file containing set of functions you want to include in your application

import scope # importing a module, to re-name a module use `import scope as sc`

class Mod:

    def test(self):
        scope.local_scope()


m = Mod()

m.test()

# There are several buil-in modules in python. Example: platform

import platform as pl

x = pl.system()
print(x)

# To print all variable and function names inside a module

print(dir(pl))

# In order to import on a variable or method from a module use below

from polymorphism import Boat

b = Boat()

b.move()