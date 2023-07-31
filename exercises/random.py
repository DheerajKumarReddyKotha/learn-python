# Random Numbers
import random

# Displays Random int number between 1 and 9
rand_int = random.randint(1, 9)
print(rand_int)

# Displays Random float number between 1 and 7
rand_float = random.uniform(1, 7)
print(rand_float)

rand_range = random.randrange(1, 10, 1)
print(rand_range)

str_list = ["Dkotha", "Mounika", "Arjun"]

# Returns random string from the list
str_choice = random.choice(str_list)
print(str_choice)

# Returns random list with weights
str_choices = random.choices(str_list, weights=[10, 1, 1], k=12)
print(str_choices)

# Shuffles the list
random.shuffle(str_list)
print(str_list)

# Returns the sub list or sample from existing
samp = random.sample(str_list, k=2)
print(samp)

# Returns random number bewteen 0 and 1
rand_num = random.random()
print(rand_num)
