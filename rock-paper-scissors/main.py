#asks Rock, paper, scissors (r/p/s): 
#computer randomly choose one of them
#print you chose whatever my choise is
#print computer chose whatever
#print either me or computer win
#asks Continue? (y/n):

import random

choices = ('r', 'p', 's')
emoji = {'r': '🪨', 'p': '📃', 's': '✂️'}

while True:
    my_choice = input("Rock, paper or scissors (r, p, or s): ").strip().lower()
    if my_choice not in choices:
        print('Invalid choice!')
        continue

    computer_choice = random.choice(choices)     

    print(f'You chose {emoji[my_choice]}')
    print(f'Computer chose {emoji[computer_choice]}')

    if my_choice == computer_choice:
        print('Tie!')
    elif (
        (my_choice == "p" and computer_choice == "r") or 
        (my_choice == "r" and computer_choice == "s") or 
        (my_choice == "s" and computer_choice == "p")):
        print('You won')
    else :
        print('You lost.')

    wants_more = input("Continue? (y/n): ").strip().lower()

    if wants_more == "n":
        break