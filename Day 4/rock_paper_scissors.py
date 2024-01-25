# Playing Rock, papper, Scissors against the computer.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

# Taking user input on their choice
user_choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. " ))
if user_choice <0 or user_choice >=3:
    print("Invalid number")
else:
    print(game_images[user_choice])

# Using random numbers to decide computer choice
computer_choice = random.randint(0,2)
print("Computer chose:\n", game_images[computer_choice])


# if statements to check if user won or lost

if user_choice == computer_choice:
    print("It's a draw ")
else:
    if user_choice == 1 and computer_choice == 0:
        print("You win. ")
    elif user_choice == 2 and computer_choice == 1:
        print("You win. ")
    elif user_choice == 0 and computer_choice == 2:
        print("You win. ")
    else:
        print("You lose. ")