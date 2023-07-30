"""
1. Operators are used to perform operations on variables and values
2. Python divides the operators inthe following groups:
    a) Arithmetic Operators
    b) Assignment Operators
    c) Comparision operators
    d) Logical operators
    e) Identity operators
    f) Membership operators
    g) Bitwise operators
"""

#Arithmetic Operators include 
"""
+  -> Addition
-  -> Subtraction
*  -> Multiplication
/  -> Division
%  -> Modulus
** -> Exponential
// -> Floor division

"""

print(10 + 12)
print(12 - 10)
print(12 * 10)
print(12 / 10)
print(12 % 10)
print(12 ** 2)
print(12 // 10)

print("=====================================================================")
#Assignment Operators include

x = 2
print(x)

x += 2
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 2
print(x)

x //= 2
print(x)

x **= 2
print(x)

print("=====================================================================")

#Comparision Operators
"""
== -> Equals
!= -> Not Equals
>  -> Greater Than
<  -> Less Than
>= -> Greater Than Equal
<= -> Less Than Equal
"""

print(1 == 1)
print(1 != 2)
print(1 > 0)
print(1 < 0)
print(1 >= 1)
print(1 <= 5)

print("=====================================================================")

#Logical Operators (`and`, `or`, `not`)
print(5>0 and 1<8)
print(5>9 or 2<1)
print(not 5 > 2)
print("=====================================================================")

#Identity Operators(`is`, `is not`)
#These are used to compare objects and check whether they are same with same memory location

x = 5
y = 5
print(x is y)

a = 5
b = 4
print(a is not b)
print("=====================================================================")

#Membership Operators (`in`,`not in`)
#It is used to test if a sequence is presented in an object

x = 5
y = [1,5,10]
z = 12

print(x in y)
print(z not in y)
print("=====================================================================")

#Bitwise operators (&,|, ^, ~, <<, >>)
"""
&  -> Sets each bit to 1 if both bits are 1
|  -> Sets each bit to 1 if one of two bits is 1
^  -> Sets each bit to 1 if only one of two bits is 1
~  -> Invert all the bits
>> -> Shift left by pushing zeros in from the right and let the leftmost bits fall off
<< -> Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""