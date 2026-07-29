'''
Number Guessing Game
'''

import random

correct_answer = random.randint(1, 100)
#print("Correct answer:", correct_answer)
user_guess = int(input("Enter your guess [1 to 100]: "))
count = 0

while (user_guess != correct_answer) and (count < 4):
    if user_guess < correct_answer:
        print("Too low!")
    else:
        print("Too high!")

    count += 1
    print("Guesses remaining:", 5-count)

    user_guess = int(input("Enter your guess again: "))

    if count == 4 and user_guess!=correct_answer:
        print("Game Over. You are out of guesses.")

if user_guess == correct_answer:
   print("Spot on!")

