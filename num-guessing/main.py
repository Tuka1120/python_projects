#print guess the number between 1 to 100
#generates random number
#if enters str print enter a valid number
#compares input with generated num if it is greater print too high
#if less print too low
#if guessed print You guessed the number, congrats.

import random
import cmath

gen_num = random.randint(1,100)

while True:
    try:
        num = int(input("guess the number between 1 to 100: "))

        if (gen_num == num):
            print("You guessed the number, congrats.")
            break
        elif gen_num > num:
            print("Too low!")
        elif gen_num < num:
            print("Too high!")
    except:
        print("Please enter a valid number")
