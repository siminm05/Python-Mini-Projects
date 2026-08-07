def main():
    word = "hangman"
    empty_spaces = []
    user_guess_list = []
    chances = 5

    for _ in word:
        empty_spaces.append("__")

    print(*empty_spaces)
    while chances > 0 and "__" in empty_spaces:
        user_guess = input("\nEnter a guess: ").lower().strip()
        if not user_guess.isalpha():
            print("\nEnter alphabets only")
            continue
        if len(user_guess) != 1:
            print("\nEnter a single alphabet")
            continue
        if user_guess in user_guess_list:
            print("\nAlready guessed the letter")
            continue
        user_guess_list.append(user_guess)
        if user_guess in word:
            for i in range(len(word)):
                if word[i].lower() == user_guess:
                    empty_spaces[i] = user_guess
            print(*empty_spaces)
        else:
            print("\nIncorrect guess")
            print(*empty_spaces)
            chances -= 1
        print("Chances left:", chances)
    if chances == 0:
        print("\nYou Lost")
    if "__" not in empty_spaces:
        print("\nYou Won")

main()
