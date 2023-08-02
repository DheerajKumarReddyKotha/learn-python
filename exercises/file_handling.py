# File Handling

"""
1. File Handling is important part of web application
2. It has several functions like creating, reading, updating and deleting files
3. key function to work with files is `open()` function
4. `open()` takes two modes `filename` and `mode`
5. There are 4 different methods: 
    a) `r` - Read
    b) `a` - Append
    c) `w` - Write
    d) `x` - Create
6. In addition we can also define the mode
    a) `t` - Text - Default value, Text Mode
    b) `b` - Binary - Binary mode(e.g images)
"""

# Syntax to open a file

f = open("demofile.txt")

f = open("demofile.txt", "rt")


# Syntax for reading file

# Read methods retuens entire content in the form of string
f.read()

# Limit number of characters to read
f.read(5)

# Read one line
f.readline()

# Read all the lines
f.readlines()

# Close file

f.close()

# Write to an existing file

# we must append parameter `a` to open method, `a` - will let you add content to end of file

f = open("demofile.txt", "a")
f.write("Add something")
f.close()

# we must append parameter `w` to open method, `a` - will let you overwrite the content

f = open("demofile.txt", "w")
f.write("Add something")
f.close()

# we must append parameter `x` to open method, `x` - will let you create new file

f = open("demofile.txt", "x")


# Delete a File

# To delete file we must import `os` module and use os.remove()

import os

os.remove("demofile.txt")

# Check if file exist

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete Folder
os.rmdir("myfolder") # We can only remove empty folders