import random
import string

user_pw_length = int(input("Enter password length: "))
#letters = "abcdefghijklmnopqrstuvwxyz"

include_lower = input("Include lowercase letters? (y/n): ").lower().strip()
include_upper = input("Include uppercase letters? (y/n): ").lower().strip()
include_digits = input("Include digits? (y/n): ").lower().strip()
include_symbols = input("Include special symbols? (y/n): ").lower().strip()

letters = ""
if include_lower == 'y':
    letters += string.ascii_lowercase
if include_upper == 'y':
    letters += string.ascii_uppercase
if include_digits == 'y':
    letters += string.digits
if include_symbols == 'y':
    letters += string.punctuation
    
# if include_symbols == 'n' and include_digits == 'n' and include_upper == 'n' and include_lower == 'n':
if letters == "":
    print("Please select at least one character type. ")
else:
    password = ""
    for _ in range(user_pw_length):
        password += random.choice(letters)

    print(password)
