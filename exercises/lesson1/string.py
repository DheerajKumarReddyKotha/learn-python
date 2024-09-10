# Using double-quotes
str = "Dkotha"
print(str)

# using single quotes
str_1 = 'Dkotha'
print(str_1)

# Using double quotes here as `'s` in single quotes would throw compilation error
str_2 = "dkotha's"
print(str_2)

# When we have to print a string in multiple lines
str_3 = """This is a very big statement 
to add it into system"""
print(str_3)

# Capitalize first character
print(str_2.capitalize())

# Returns casefold copy of string
print("ß".casefold())

# Returns String in middle of 20 characters appending fill character before and after the String
print("DKOTHA".center(20, '$'))

# Returns length of the string
print("DKOTHA".__len__())

# Checks whether `kot` is present in `DKOTHA`
print("kot" in "DKOTHA")

# Checks whether `kot` is not present in `DKOTHA`
print("kot" not in "DKOTHA")

# Checks whether String provided ends with character asked in the method
print("DKOTHA".endswith("A"))

# Finds the index of first apearance of character in the string
print("DKOTAHA".find("A", 2))

# Perform String formatting operation
print("DKOTHA AGE IS 23 + 9 WHICH IS {0} WHO IS BORN IN {1}".format(23 + 9, 1992))

# Returns lowest index of character
print("DKOTHA".index("K"))

# Returns true if the string is a decimal
print("23".isdecimal())

# Returns true if the string is a digit
print("123".isdigit())

# Returns true if the string is in lowercase
print("DKOTHA".islower())

# Returns true if the string is in uppercase
print("DKOTHA".isupper())

# Returns True if the string is all characters are white spaces
print("     ".isspace())

print("     putty   p")

# Strips all the white spaces to the left
print("     putty   p".lstrip())

# This returns a TUPLE with everything before match, match word and after match
print("DKOTHA is drinking milk".partition("is"))

# Returns the string replacing the character
print("DKOTHA".replace('D', 'P'))

# Returns sub-string
print("DKOTHA"[2:5])
