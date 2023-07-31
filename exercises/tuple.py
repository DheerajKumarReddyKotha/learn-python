# Tuples

"""
1. Tuples are a collection which is ordered and unchangeable.
2. Tuples are written with rounded brackets.
3. Tuples are used to store multiple values in a single variable.
4. We cannot add or remove or change items in the tuple.
5. Tuples allow duplicates.
6. Tuples can contain values of any data types.
7. We can also create tuple using constructor. tuple()
"""

# 1. Create Tuples

t = ("Apple", "Cat", "Banana")
print(t)

# Length of tuple 
print(len(t))

# Tuple with one item, always use `,` after adding item otherwise python recognizes it as `String`
t_1 = ("Bat",)
print(t_1)
print(type(t_1))

# Tuple creation using constructor
t_c = tuple(("Mounika","Dheeraj"))
print(t_c)

print("=====================================================================")

# 2. Access Tuple items

# Retrieve based on index
print(t[1])

# Retrieves Sub-list starting from index 1 included and 3 excluded
print(t[1:3])

# Retrieves Sub-list starting from index 1 till end of List
print(t[1:])

# Retrieves Sub-list starting from index 0 included and 3 excluded
print(t[:3])

# Negative Indexing, -1 refers to last item in the list
print(t[-1])
print("=====================================================================")

# 3. Update Tuple items

# Inorder to update Tuple items convert them to list and then update and convert back to tuple.

# 4. Unpack Tuples

# When create tuples, we assign values to it. It is called `Packing`.
t_p = (1, 2, 7, 9)

# When we extract tuple values back to variables is known as `UnPacking`
# Number of values must match number of variables, else use * that collects values to list
(one, two, three, four) = t_p
print(one)

# Use `*` for storing remaining values to a list variable
(one, *two) = t_p
print(one)
print(*two)

(one, *two, three) = t_p
print(one)
print(*two)
print(three)

print("=====================================================================")

# 5. Loop Tuples
t_loop = ("A", "B", "C")

# For Loop
for l in t_loop:
    print(l)

for l in range(len(t_loop)):
    print(t_loop[l])

# While Loop
i = 0
while i < len(t_loop):
    print(t_loop[i])
    i += 1

# Tuple Comprehension
[print(x) for x in t_loop]

print("=====================================================================")

# 6. Join Tuples

t_j1 = (1, 2, 4, 5)
t_j2 = (6, 7, 9, 52)

t_join = t_j1 + t_j2  # We can also use `extend` keyword
print(t_join)

# Multiple content in the tuple
t_m = t_j1 * 2
print(t_m)

print("=====================================================================")

# 7. Tuple Methods
"""
count()	- Returns the number of times a specified value occurs in a tuple
index()	- Searches the tuple for a specified value and returns the position of where it was found
"""