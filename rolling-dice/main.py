
#ask roll the dice press y,Y to accept or n,N to reject
#ask how many dices they want to roll from 1 to 10
#if accepts generate two random number from 1 to 6.
#keeps the track how many times user rolled the dice
#if presses n,N print 'thank you for playing'

import random

while True:
    choice = input("Roll the dice? (y/n): ").strip().lower()
    if choice == 'y':
        try:
            dices = int(input("How many dices do you want to roll? choose from (1 to 10): "))
            for _ in range(dices):
                print(random.randint(1,6))
            break
        except ValueError:
            print("invalid input. Please enter number from 1 to 10.")
    elif choice == 'n':
        print("thank you for playing")
        break
    else:
        print("Invalid input. Please press 'y' or 'n'.")
