import random

computer_choice = random.choice(["rock","paper","scissors"])
user_choice = input("Do you want rock, papaer or scissors?\n")

if(computer_choice == user_choice):
    print("TIE")
elif(user_choice == "rock" and computer_choice == "scissors"):
    print("you WIN")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("you WIN")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("you WIN")
else:
    print("you LOOSE")