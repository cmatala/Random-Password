import string
import random

# input the length of the password
length = int(input("Password Length: "))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

combined = symbols + upper + lower + num

temp = random.sample(combined, length)
password = "".join(temp)

print(password)
