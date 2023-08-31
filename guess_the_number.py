# This is a Python "Guess the Number" game
# To enter an EMOJI, hold down the WIN key and hit the ';' key

import random
import os
import time
from color_text import *

os.system("cls")

guessesTaken = 0
guess = "?"

myName = input("Hello! What is your name? ")
high = int(input(f"{myName}, what maximum number would you like? "))
low = 1

number = random.randint(1, high)

while guess != number:
    os.system("cls")
    print(f'Well, {myName}, I am thinking of a number between {low} and {high}.')

    guessesTaken += 1
    guess = int(input(f'Make guess #{guessesTaken}: '))

    if guess < number:
        print(f"{BLUE}Your guess is too low.{DEFAULT}")
        if guess > low:
            low = guess

    if guess > number:
        print(f"{RED}Your guess is too high.{DEFAULT}")
        if guess < high:
            high = guess

    time.sleep(1)

if guess == number:
    # guessesTaken = str(guessesTaken)
    print(
        f"{RED}Good job, {myName} 😀😀. You guessed my number in {guessesTaken} guesses!{DEFAULT}")

print()
