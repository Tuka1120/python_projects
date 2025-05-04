#asks Rock, paper, scissors (r/p/s): 
#computer randomly choose one of them
#print you chose whatever my choise is
#print computer chose whatever
#print either me or computer win
#asks Continue? (y/n):

import random

choices = ('r', 'p', 's')
emoji = {'r': '🪨', 'p': '📃', 's': '✂️'}

def get_user_choice():
    while True:
        user_choice = input("Rock, paper or scissors (r, p, or s): ").strip().lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choice(user_choice, computer_choice):
    print(f'You chose {emoji[user_choice]}')
    print(f'Computer chose {emoji[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == "p" and computer_choice == "r") or 
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "s" and computer_choice == "p")):
        print('You won')
    else :
        print('You lost.')
        
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)     

        display_choice(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        wants_more = input("Continue? (y/n): ").strip().lower()

        if wants_more == "n":
            break


play_game()