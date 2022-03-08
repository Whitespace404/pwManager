from cryptography.fernet import Fernet
from os import environ

ENCODING = "utf-8"

key = bytes(environ.get("PWM_KEY"), ENCODING)
cryptography = Fernet(key)


def encrypt(password):
    encrypted = cryptography.encrypt(bytes(password, ENCODING))
    return encrypted


def decrypt(encrypted_str):
    decrypted = cryptography.decrypt(encrypted_str)
    return decrypted.decode(ENCODING)
