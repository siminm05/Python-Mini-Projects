'''
Number Guessing Game
'''

import random

correct_answer = random.randint(1, 100)
#print("Correct answer:", correct_answer)
user_guess = int(input("Enter a num [1 to 100]: "))

if user_guess == correct_answer:
    print("Spot on!")
elif user_guess < correct_answer:
    print("Too low!")
else:
    print("Too high!")
