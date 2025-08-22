import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO User (username, user_password, user_email) VALUES (?, ?, ?)",
            ('Admin', 'abc', 'admin@info.com')
            )

connection.commit()
connection.close()