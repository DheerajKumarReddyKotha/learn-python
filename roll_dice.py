import random

roll = random.randint(1,6)
guess = int(input("Guess the Dice roll:\n"))

if(guess == roll):
    print("Correct! They rolled a "+str(roll))
else:
    print("Wrong! They rolled a "+str(roll))
