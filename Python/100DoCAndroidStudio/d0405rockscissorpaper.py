# import random

# hand = ['rock', 'paper', 'scissor']

# random_hand = random.shuffle(hand)

# print = input(suit)

# if random_hand == ['rock']
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        user_choice = user_choice.lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid input. Please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()
