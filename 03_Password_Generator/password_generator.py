import random
import string

user_pw_length = int(input("Enter password length: "))
#letters = "abcdefghijklmnopqrstuvwxyz"
lower_letters = string.ascii_lowercase
i = 0
password = ""
for i in range(user_pw_length):
    password = password + random.choice(lower_letters)
    i+=1

print(password)
