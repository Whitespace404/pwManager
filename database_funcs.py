import sqlite3

conn = sqlite3.connect("vault.db")
cursor = conn.cursor()


def create_table():
    sql = """CREATE TABLE passwords (
        url text,
        password text,
        email text,
        username text
    )"""
    cursor.execute(sql)

    conn.commit()
    conn.close()


def add_values(url, password, email, username):
    values_list = (url, password, email, username)
    sql = """INSERT INTO passwords VALUES (
        ?, ?, ?, ?
    )"""
    cursor.execute(sql, values_list)

    conn.commit()
    conn.close()


def show_all_passwords():
    sql = "SELECT * FROM passwords"
    response = cursor.execute(sql).fetchall()
    return response


def get_by_url(url):
    sql = "SELECT * FROM passwords WHERE url=:url"
    response = cursor.execute(sql, {"url": url}).fetchall()
    return response


def delete_by_url(url):
    sql = "DELETE FROM passwords WHERE url=:url"
    cursor.execute(sql, {"url": url})

    conn.commit()
    conn.close()


def edit_by_url(url, column, value):
    sql = f"UPDATE passwords SET {column} = {value} WHERE url={url}"
    cursor.execute(sql)

    conn.commit()
    conn.close()


def drop_passwords_table():
    sql = "DROP TABLE passwords;"
    cursor.execute(sql)

    conn.commit()
    conn.close()