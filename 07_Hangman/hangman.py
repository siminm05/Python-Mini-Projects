import random


def main():
    words = ["Elephant", "Chocolate", "Mountain", "Umbrella", "Adventure",
            "Basketball", "Butterfly", "Strawberry", "Television"]
    empty_spaces = []
    user_guess_list = []
    chances = 5

    answer = random.choice(words)

    for _ in answer:
        empty_spaces.append("__")

    print("\n", *empty_spaces)
    while chances > 0 and "__" in empty_spaces:
        user_guess = input("Enter a guess: ").lower().strip()
        if not user_guess.isalpha():
            print("Enter alphabets only\n")
            continue
        if len(user_guess) != 1:
            print("Enter a single alphabet\n")
            continue
        if user_guess in user_guess_list:
            print("Already guessed the letter\n")
            continue
        user_guess_list.append(user_guess)
        if user_guess in answer.lower():
            for i in range(len(answer)):
                if answer[i].lower() == user_guess:
                    empty_spaces[i] = user_guess
            print(*empty_spaces)
        else:
            print("Incorrect guess\n")
            print(*empty_spaces)
            chances -= 1
        print("Chances left:", chances)
        print("Guessed letters:", *user_guess_list)
    if chances == 0:
        print("\nYou Lost")
        print("Answer:", answer)
    if "__" not in empty_spaces:
        print("\nYou Won")

main()
