import sqlite3

db = sqlite3.connect("harajadlar/xarajatlar.db")
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS xarajatlar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kategoriya VARCHAR(100),
        summa REAL,
        sana DATE
    )
""")

db.commit()