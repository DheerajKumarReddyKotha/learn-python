expenses = [12, 34, 56, 34, 89.4, 34.8]

sum_ = 0
for expense in expenses:
    sum_ += expense #We can also use `sum` function

print("You spent: $",sum_, sep ='') #separator is used between print string and it's value

input_list = range(0,7,1) #0 is start, 7 is stop and 1 is a step

expenses_new = []
for i in range(7): #Range is used to iterate the values
    expenses_new.append(float(input("Enter an expense:")))

total = sum(expenses_new)
print("You spent: $",total, sep ='') #separator is used between print string and it's value
