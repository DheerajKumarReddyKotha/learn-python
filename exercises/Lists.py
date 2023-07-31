# Lists
"""
1. Lists are used to store multiple items into single variable
2. Lists are one of the 4 built-in data types in python used to store collection of data
3. Lists are created using []
4. List can hold values irrespective of data type
5. Lists are ordered that means the order of items will not change, and changeable means items can be added and removed,new items will be added at the end
6. Lists are changeable meaning items in the list can be added/removed
7. List allow duplicates
"""

# 1. Create Lists
list_l = [1, "2", 3, 3.7]
print(list_l)
print("=====================================================================")

# 2 Access list items

# Retrieve based on index
print(list_l[1])

# Retrieves Sub-list starting from index 1 included and 3 excluded
print(list_l[1:3])

# Retrieves Sub-list starting from index 1 till end of List
print(list_l[1:])

# Retrieves Sub-list starting from index 0 included and 3 excluded
print(list_l[:3])

# Negative Indexing, -1 refers to last item in the list
print(list_l[-1])
print("=====================================================================")

# 3. Change List items
list_l[1] = 12.5
print(list_l)

list_l[1:3] = ["11", 15.6]
print(list_l)

# Inserts values without replacing any existing values
list_l.insert(2, "Watermelon")
print(list_l)
print("=====================================================================")

# 4. Add List items
list_l.append("Pineapple")
print(list_l)

# Add another list to existing list using `extend`, it also allows to add elemets from `tuple`,`set, dictionaries etc`
list_existing = [1, 2, 3, 4]
list_new = [5, 6, 7, 8]

list_existing.extend(list_new)
print(list_existing)

print("=====================================================================")

# 5. Remove List items
list_remove = [5, 6, 7, 8]

# Removes specified item
list_remove.remove(6)
print(list_remove)

# Removes value from specified index
list_remove.pop(1)
print(list_remove)

del list_remove[0]
print(list_remove)

# List still exist but entries are removed
list_remove.clear()
print(list_remove)

# Deletes entire List
del list_remove

print("=====================================================================")

# 6. Loop Lists
list_loop = ["A", "B", "C"]

# For Loop
for l in list_loop:
    print(l)

for l in range(len(list_loop)):
    print(list_loop[l])

# While Loop
i = 0
while i < len(list_loop):
    print(list_loop[i])
    i += 1

# List Comprehension
[print(x) for x in list_loop]

print("=====================================================================")

# 7. Sort Lists

# Sort method will sort list items alphanumerically and ascending by default

list_alpha = ["Apple", "Cat", "Boy", "Dog"]
list_alpha.sort()
print(list_alpha)

list_num = [1, 5, 2, 9, 4, 0]
list_num.sort()
print(list_num)

# Sort descending
list_alpha.sort(reverse=True)
print(list_alpha)

list_num.sort(reverse=True)
print(list_num)

"""
1. We can also Customize sort function
2. Case insensitive sorting gives unexpected results, sort() is case sensitive where all upper case letters are sorted before lower case letters.
"""

print("=====================================================================")

# 8. Copy Lists

# We cannot copy a list by simple assigning list_1 = list_2 because any changes in list_1 will also impact list_2

list_1 = [1, 2, 4, 5]
list_2 = list_1.copy()  # We can also use list_2 = list(list_1)

list_1.pop(0)
print(list_1)
print(list_2)

print("=====================================================================")

# 9. Join Lists

list_j1 = [1, 2, 4, 5]
list_j2 = [6, 7, 9, 52]

list_join = list_j1 + list_j2  # We can also use `extend` keyword
print(list_join)

print("=====================================================================")

# 10. List Methods
"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
