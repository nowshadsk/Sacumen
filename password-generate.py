import random
import string

length = int(input("enter password length : "))
if length >= 8:
    length = length
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    special_character = 0
    punctuation = r"""!#$%&*+-=?@^_|"""
    special_character = punctuation
    characters = upper + lower + digit + special_character
    for i in characters:
        for j in i:
            if j != i:
                characters = characters
            else:
                continue
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is :", password)
else:
    print("invalid input. Password length must be at least 8")
