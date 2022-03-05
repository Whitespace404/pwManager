import sqlite3

conn = sqlite3.connect("vault.db")
cursor = conn.cursor()

def create_db():
    sql = """CREATE TABLE passwords (
        url text,
        password text,
        email text
    )"""
    cursor.execute(sql)

def add_password(url, password, email):
    sql = f"""INSERT INTO passwords VALUES (
        '{url}',
        '{password}',
        '{email}'
    )"""
    cursor.execute(sql)

def show_all_passwords():
    sql = f"SELECT * FROM passwords"
    return cursor.execute(sql).fetchall()
