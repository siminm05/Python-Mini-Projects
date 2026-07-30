'''
Number Guessing Game
'''
import random


def get_difficulty():
    try:
        numOfChances = 0
        user_difficulty = int(input("1. Easy\n2. Medium\n3. Hard\nSelect Difficulty: "))
        if user_difficulty == 1:
            numOfChances = 10
        elif user_difficulty == 2:
            numOfChances = 7
        elif user_difficulty == 3:
            numOfChances = 5
        else:
            print("Invalid Input. Enter a Number [1 to 3]")
            return None

    except ValueError:
        print("Enter a Number [1 to 3]")
        return None

    return numOfChances

def gameplay(numOfChances):
    correct_answer = random.randint(1, 100)
    # print("Correct answer:", correct_answer)

    user_guess = 0
    count = 0

    while (user_guess != correct_answer) and (count < numOfChances):
        try:
            user_guess = int(input("Enter your guess [1 to 100]: "))

            if user_guess < correct_answer:
                print("Too low!")
            elif user_guess == correct_answer:
                print("Spot on!")
            else:
                print("Too high!")

            count += 1
            # print("Count: ", count)

            if count == numOfChances and user_guess != correct_answer:
                print("Game Over. You are out of guesses.")
                break

            if count < numOfChances and user_guess != correct_answer:
                print("Guesses remaining:", numOfChances - count)

        except ValueError:
            print("Enter Int only")


def main():
    while True:
        numOfChances = get_difficulty()
        if numOfChances is None:
            return

        gameplay(numOfChances)


        new_game = input("Would you like to play again? (yes/no): ").lower().strip()

        if new_game == 'yes':
            continue
        elif new_game == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input")
            break

main()
