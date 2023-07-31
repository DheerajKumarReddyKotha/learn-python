# Sets

"""
1. Sets are used to store multiple items in a single variable
2. Set is a collection which is unordered and unindexed
3. Sets are written within curly braces
4. Set do not allow duplicates
"""

# 1. Create a Set
s = {1, 4, "D", 3.8, 4}
print(s)

s_con = set((1, 4, "M", "U"))
print(s_con)

print("=====================================================================")

# 2. Access Set items

for x in s:
    print(x)

print("=====================================================================")

# 3. Add items to Set

s.add("Dkotha")
print(s)

# Add items from another Set or List

s_a = {"Orange", "Apple"}
s.update(s_a)
print(s)

print("=====================================================================")

# 4. Remove Set items
s_remove = {5, 6, 7, 8}

# Removes specified item
s_remove.remove(6) # We can also use `discard()`
print(s_remove)

# Removes value from Set
s_remove.pop()
print(s_remove)

# List still exist but entries are removed
s_remove.clear()
print(s_remove)

# Deletes entire List
del s_remove

print("=====================================================================")

# 5. Loop Sets
for x in s:
    print(x)

print("=====================================================================")

# 6. Join Sets

s_j1 = {"Apple", "Banana"}
s_j2 = {"Canberry", "Donut"}

s_ju = s_j1.union(s_j2)
print(s_ju)

s_j1.update(s_j2)
print(s_j1)

print("=====================================================================")

# 7. Set methods
"""
add()	                Adds an element to the set
clear()	                Removes all the elements from the set
copy()	                Returns a copy of the set
difference()	        Returns a set containing the difference between two or more sets
difference_update()	    Removes the items in this set that are also included in another, specified set
discard()	            Remove the specified item
intersection()	        Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        Returns whether two sets have a intersection or not
issubset()	            Returns whether another set contains this set or not
issuperset()	        Returns whether this set contains another set or not
pop()	                Removes an element from the set
remove()	            Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                Return a set containing the union of sets
update()	            Update the set with the union of this set and others
"""