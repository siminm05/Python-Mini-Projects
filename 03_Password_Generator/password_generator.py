import random
import string

user_pw_length = int(input("Enter password length: "))
#letters = "abcdefghijklmnopqrstuvwxyz"
letters = string.ascii_letters + string.digits
password = ""
for _ in range(user_pw_length):
    password += random.choice(letters)

print(password)
