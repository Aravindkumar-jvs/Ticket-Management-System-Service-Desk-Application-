# import sqlite3

# conn = sqlite3.connect("tickets.db")

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS tickets (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     issue TEXT,
#     priority TEXT,
#     status TEXT
# )
# """)

# conn.commit()

# conn.close()

# print("Database Created Successfully")2

import sqlite3

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    issue TEXT,
    category TEXT,
    priority TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")