'''
Number Guessing Game
'''

import random

correct_answer = random.randint(1, 100)
#print("Correct answer:", correct_answer)
user_guess = int(input("Enter your guess [1 to 100]: "))

while (user_guess != correct_answer):
    if user_guess < correct_answer:
        print("Too low!")
    else:
        print("Too high!")

    user_guess = int(input("Enter your guess again: "))

if user_guess == correct_answer:
   print("Spot on!")

