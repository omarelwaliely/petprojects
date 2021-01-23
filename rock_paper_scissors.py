import random
from random import randint

random.seed()
computer_choice = randint(1, 3)
user_choice = input("Rock Paper or Scissors? ").lower()


def game():
    if computer_choice == 1 and user_choice == "rock":
        print("Computer did: Rock")
        print("Tie, Everybody Loses!")
    elif computer_choice == 1 and user_choice == "paper":
        print("Computer did: Rock")
        print("You Won!")
    elif computer_choice == 1 and user_choice == "scissors":
        print("Computer did: Rock")
        print("You Lost!")
    elif computer_choice == 2 and user_choice == "rock":
        print("Computer did: Paper")
        print("You Lost!")
    elif computer_choice == 2 and user_choice == "paper":
        print("Computer did: Paper")
        print("Tie, Everybody Loses!")
    elif computer_choice == 2 and user_choice == "scissors":
        print("Computer did: Paper")
        print("You Win!")
    elif computer_choice == 3 and user_choice == "rock":
        print("Computer did: Scissors")
        print("You Win!")
    elif computer_choice == 3 and user_choice == "Scissors":
        print("Computer did: Scissors")
        print("Tie, Everybody Loses!")
    elif computer_choice == 3 and user_choice == "paper":
        print("Computer did: Scissors")
        print("You Lose!")
    elif not user_choice:
        print("Do you not know how to type or something?")
    else:
        print(f"{user_choice} is not a valid statment dude...")


game()
