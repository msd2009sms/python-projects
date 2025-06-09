import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Type Q to quit : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0 , 2)
    computer_input = options[random_number]

    if user_input == "rock" and computer_input == "scissors":
        print("You Won !")
        user_wins += 1

    elif user_input == "paper" and computer_input == "rock":
        print("You Won !")
        user_wins += 1

    elif user_input == "scissors" and computer_input == "paper":
        print("You Won !")
        user_wins += 1

    else:
        print("You Lost !")
        computer_wins += 1

print("You Won", user_wins, "times.")
print("Computer Won", computer_wins, "times.")
print("Goodbye!")