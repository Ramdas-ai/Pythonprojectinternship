# CODSOFT - TASK 4: ROCK-PAPER-SCISSORS

import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def find_winner(user, comp):
    if user == comp:
        return "tie"
    if (user == "rock" and comp == "scissors") or \
       (user == "paper" and comp == "rock") or \
       (user == "scissors" and comp == "paper"):
        return "user"
    return "computer"

while True:
    user = input("\nEnter rock/paper/scissors or quit: ").lower()

    if user == "quit":
        print("Final Score → You:", user_score, "| Computer:", computer_score)
        break

    if user not in choices:
        print("Invalid input!")
        continue

    comp = random.choice(choices)
    print("Computer chose:", comp)

    winner = find_winner(user, comp)

    if winner == "user":
        print("You win!")
        user_score += 1
    elif winner == "computer":
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a tie.")
