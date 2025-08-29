import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

default_users = [
    ('admin', 'admin', 'admin@info.com'),
    ('demo', 'demo', 'demo@info.com'),
]

cur.executemany("INSERT INTO User (username, user_password, user_email) VALUES (?, ?, ?)", default_users)

demo_id = cur.lastrowid

default_products = [
    ('C100 - Farming', demo_id),
    ('C101 - Soils', demo_id)
]

cur.executemany("INSERT INTO Product (title, created_by) VALUES (?, ?)", default_products)

# Obtain Products Created
cur.execute("SELECT id FROM Product WHERE created_by = ? ORDER BY id ASC", (demo_id))
product_ids = [row[0] for row in cur.fetchall()]

first_product_id = product_ids[0]
packs_data = [
    ('Star Dew Valley', first_product_id),
    ('Seeds & you', first_product_id),
    ('Crop Rotations', first_product_id)
]

cur.executemany("INSERT INTO Pack (title, product_id) VALUES (?, ?)", packs_data)

cur.execute("SELECT id FROM Pack WHERE product_id = ? ORDER BY id ASC", (first_product_id))
pack_ids = [row[0] for row in cur.fetchall()]

first_pack_id = pack_ids[0]
lessons_data = [
    ('Lesson 1: Buying the game', first_pack_id),
    ('Lesson 2: Enjoying the game', first_pack_id),
    ('Lesson 3: ???', first_pack_id),
    ('Lesson 4: Profit', first_pack_id)
]
cur.executemany("INSERT INTO Lesson (content, pack_id) VALUES (?, ?)", lessons_data)

connection.commit()
connection.close()