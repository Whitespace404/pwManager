import sqlite3

connection = sqlite3.connect("secrets.db")
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE secrets (
#                   account text,
#                   username text,
#                   password text
# )""")

# cursor.execute("""INSERT INTO secrets VALUES (
#                 'github', 'test', '123'
#                 )""")

# connection.commit()

# cursor.execute("SELECT * FROM secrets")
# print(cursor.fetchall())

master_password = input("Enter master password: ")
if master_password != "test":
    quit()

print("Welcome to password manager.")

print("""
Would you like to:

1: View all passwords
2: Add a new password
3: Delete a password
4: Update a password
""")
