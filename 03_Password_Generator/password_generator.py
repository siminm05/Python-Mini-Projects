import random
import string

user_pw_length = int(input("Enter password length: "))
#letters = "abcdefghijklmnopqrstuvwxyz"
letters = string.ascii_letters
#i = 0
password = ""
for _ in range(user_pw_length):
    password = password + random.choice(letters)

print(password)
