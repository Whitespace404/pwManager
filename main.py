import os
from time import sleep

import clipboard

import encrypt_funcs
import database_funcs as db

print("""
1: Add password
2: View password
3: Edit password
4: Delete password
""")
choice = int(input("> "))

if choice == 1:
    account = input("Enter the URL to the website: ")
    password = input("Enter the password: ")
    email = input("Enter the email adress you used: ")
    username = input("Enter the username you provided: ")

    db.add_values(account, encrypt_funcs.encrypt(password), email, username)
    print("Done.")

elif choice == 2:
    account = input("Enter the URL to the website: ")
    data = db.get_by_url(account)
    password = encrypt_funcs.decrypt(data[0][1])
    if data:
        print(f"Showing passwords for {data[0][2]} on {data[0][0]}")
        print(f"Password: {password}")
        print(f"Username: {data[0][3]}")

        copy = input("Would you like to copy the password to your clipboard? ")
        if copy == "y":
            clipboard.copy(password)
            print("Your clipboard and terminal window will be cleared in 10 seconds")
            sleep(10)
            clipboard.copy(" ")
            os.system("cls")
        else:
            sleep(10)
            os.system("cls")
    else:
        print(f"{account} was not found.")

elif choice == 4:
    account = input("Enter the URL to the website: ")

    sure = input("Are you sure you want to delete it? (y/n) ")

    if sure == "y":
        data = db.delete_by_url(account)
        print("Deleted.")
    else:
        print("Not deleted.")

else:
    print("""1: Add password
2: View password
3: Edit password
4: Delete password""")
