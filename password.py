import random
import string

print ('Welcome to password generator')
try:
    n = int(input('How many numbers do you want ? '))
    l = int(input("How many letters do you want ? "))
    c = int(input("How many capital letters do you want ? "))
    s = int(input('How many symbols do you want to have in your password ? '))
except ValueError:
        print("Please enter valid numbers.")
        exit()
let = random.choices(string.ascii_lowercase, k = l)
cap = random.choices(string.ascii_uppercase, k = c)
r = random.choices(string.digits, k = n)
sym = random.choices(string.punctuation, k = s)

p = (let+ r + sym + cap)
random.shuffle(p)

password = "".join(p)
print("Generated Password:", password)
