import random

computer_choice = random.choice(["rock", "paper", "scissors"])

user_choice = input("Suit yuk (rock, paper, scissors): ")
user_choice = user_choice.lower()

if user_choice == computer_choice:
    print("Imbang")
elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "scissors" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
    print("Anda menang!")
else:
    print("komputer menang")


print(f'Computer chose: {computer_choice}')
print(f'You chose: {user_choice}')
#print(winner(user_choice, computer_choice))

#play_game()