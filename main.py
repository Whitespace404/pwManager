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

# cursor.execute("SELECT * FROM secrets")
# print(cursor.fetchall())
