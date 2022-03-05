from random import choice
import string

PASSWORD_CHARACTERS = string.ascii_letters + string.digits + string.punctuation

def generate_password(characters):
    password = ""

    for character in range(1, characters + 1):
        password += choice(PASSWORD_CHARACTERS)

    return password
