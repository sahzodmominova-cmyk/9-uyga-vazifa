import sqlite3

db = sqlite3.connect("crm.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism TEXT,
    telefon TEXT,
    email TEXT,
    kompaniya TEXT
)
""")

db.commit()