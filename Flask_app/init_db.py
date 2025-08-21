import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO User (username, user_password) VALUES (?, ?)",
            ('Admin', 'abc')
            )

connection.commit()
connection.close()