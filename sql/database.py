import sqlite3

db = sqlite3.connect("sql/ombor.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mahsulotlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nomi TEXT,
    narx INT,
    miqdor INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM mahsulotlar")

if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO mahsulotlar (nomi, narx, miqdor)
    VALUES (?, ?, ?)
    """, [
        ("Kompyuter", 5000000, 3),
        ("Sichqoncha", 50000, 10),
        ("Klaviatura", 150000, 5),
        ("Monitor", 1500000, 4)
    ])

db.commit()