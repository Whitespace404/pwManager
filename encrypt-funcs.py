from cryptography.fernet import Fernet
from os import environ

key = bytes(environ.get("PWM_KEY"), "utf-8")
cryptography = Fernet(key)

def encrypt(password):
    encrypted = cryptography.encrypt(bytes(password, "utf-8"))
    return encrypted
