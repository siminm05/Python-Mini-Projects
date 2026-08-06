word = []
empty_spaces = []
user_guess_list = []

answer = "hangman"

i = 0
while i != len(word):
    empty_spaces.append("__")
    i += 1

print(*empty_spaces)
chances = 5
while "__" in empty_spaces:
    if chances != 0:
        user_guess = input("Enter a guess: ").lower().strip()
        if user_guess not in user_guess_list:
            user_guess_list.append(user_guess)
            if user_guess in word:
                for i in range(len(word)):
                    if word[i].lower() == user_guess:
                        empty_spaces[i] = user_guess
                print(*empty_spaces)
            else:
                print("Incorrect guess")
                print(*empty_spaces)
                chances -= 1
            print("Chances left:", chances)
        else:
            print("Already guessed the letter:", user_guess)
    elif chances == 0 and "__" in empty_spaces:
        print("You Lost")
        break
    if "__" not in empty_spaces:
        print("You Won")
