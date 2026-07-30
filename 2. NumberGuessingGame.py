'''
Number Guessing Game
'''

import random

correct_answer = random.randint(1, 100)
#print("Correct answer:", correct_answer)

user_guess = 0
count = 0

while (user_guess != correct_answer) and (count < 5):
    try:
        user_guess = int(input("Enter your guess [1 to 100]: "))

        if user_guess < correct_answer:
            print("Too low!")
        elif user_guess == correct_answer:
            print("Spot on!")
        else:
            print("Too high!")

        count += 1

        if count == 5 and user_guess != correct_answer:
            print("Game Over. You are out of guesses.")
            break

        # print("Count: ",count)
        if count < 5 and user_guess != correct_answer:
            print("Guesses remaining:", 5 - count)

    except ValueError:
        print("Enter Int only")
