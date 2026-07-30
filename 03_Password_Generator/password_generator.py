import random
import string

def get_answer(question):
    while True:
        answer = input(question).lower().strip()
        if answer in ['y', 'n']:
            return answer
        else:
            print("Enter y/n: ")

def get_letters():
    include_lower = get_answer("Include lowercase letters? (y/n): ")
    include_upper = get_answer("Include uppercase letters? (y/n): ")
    include_digits = get_answer("Include digits? (y/n): ")
    include_symbols = get_answer("Include special symbols? (y/n): ")

    letters = ""

    if include_lower == 'y':
        letters += string.ascii_lowercase
    if include_upper == 'y':
        letters += string.ascii_uppercase
    if include_digits == 'y':
        letters += string.digits
    if include_symbols == 'y':
        letters += string.punctuation

    return letters

def password_generate():
    try:
        numOfPasswords = int(input("How many passwords you want to generate: "))
        i = 0
        user_pw_length = int(input("Enter password length: "))
        # letters = "abcdefghijklmnopqrstuvwxyz"

        letters = get_letters()

        if 0 >= user_pw_length or user_pw_length > 20:
            print("Password Length should be between 1 to 0")
        elif numOfPasswords < 0:
            print("Enter a number greater than 0")
            # if include_symbols == 'n' and include_digits == 'n' and include_upper == 'n' and include_lower == 'n':
        elif letters == "":
            print("Please select at least one character type. ")
        else:
            for i in range(numOfPasswords):
                password = ""
                for _ in range(user_pw_length):
                    password += random.choice(letters)
                
                print(i+1, ". ", password, sep="")

    except ValueError:
        print("Invalid input type")

def main():
    while True:
        password_generate()

        new_password = input("Do you want to generate a new password? (y/n)").lower().strip()
        if new_password == 'y':
            continue
        else:
            print("Thank you.")
            break

main()
