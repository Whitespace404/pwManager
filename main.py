import sqlite3

db = sqlite3.connect("secrets.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE passwords (account text, 
                        password text,
                        email text,
                        url text)""")

