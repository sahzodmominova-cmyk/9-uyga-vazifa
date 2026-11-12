import sqlite3

db = sqlite3.connect("kutubxona.db")
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(100),
        muallif VARCHAR(100),
        holat VARCHAR(20)
    )
""")
db.commit()

cursor.execute("SELECT COUNT(*) FROM books")
if cursor.fetchone()[0] == 0:
    sample_books = [
        ('Otkan kunlar', 'Abdulla Qodiriy', 'mavjud'),
        ('Mehrobdan chayon', 'Abdulla Qodiriy', 'mavjud'),
        ('Ikki eshik orasi', 'Otkir Hoshimov', 'mavjud'),
        ('Sariq devni minib', 'Xudoyberdi Toxtaboyev', 'mavjud')
    ]
    cursor.executemany("INSERT INTO books (nom, muallif, holat) VALUES (?, ?, ?)", sample_books)
    db.commit()

def mavjud_kitoblar():
    cursor.execute("SELECT id, nom, muallif FROM books WHERE holat = 'mavjud'")
    kitoblar = cursor.fetchall()
    print("\n--- Mavjud kitoblar ---")
    if not kitoblar:
        print("Hozirda mavjud kitoblar yo'q.")
    for k in kitoblar:
        print(f"ID: {k[0]} | Nomi: {k[1]} | Muallif: {k[2]}")

def kitob_band_qilish():
    mavjud_kitoblar()
    kitob_id = input("\nBand qilmoqchi bo'lgan kitob ID raqamini kiriting: ")
    cursor.execute("SELECT holat FROM books WHERE id = ?", (kitob_id,))
    kitob = cursor.fetchone()
    
    if kitob:
        if kitob[0] == 'mavjud':
            cursor.execute("UPDATE books SET holat = 'band' WHERE id = ?", (kitob_id,))
            db.commit()
            print("Kitob muvaffaqiyatli band qilindi!")
        else:
            print("Bu kitob allaqachon band qilingan!")
    else:
        print("Bunday ID raqamdagi kitob topilmadi.")

def kitob_qaytarish():
    cursor.execute("SELECT id, nom, muallif FROM books WHERE holat = 'band'")
    kitoblar = cursor.fetchall()
    print("\n--- Band qilingan kitoblar ---")
    if not kitoblar:
        print("Hozirda band qilingan kitoblar yo'q.")
        return
    for k in kitoblar:
        print(f"ID: {k[0]} | Nomi: {k[1]} | Muallif: {k[2]}")
        
    kitob_id = input("\nQaytarib bermoqchi bo'lgan kitob ID raqamini kiriting: ")
    cursor.execute("SELECT holat FROM books WHERE id = ?", (kitob_id,))
    kitob = cursor.fetchone()
    
    if kitob:
        if kitob[0] == 'band':
            cursor.execute("UPDATE books SET holat = 'mavjud' WHERE id = ?", (kitob_id,))
            db.commit()
            print("Kitob muvaffaqiyatli qaytarib olindi!")
        else:
            print("Bu kitob band qilinmagan edi!")
    else:
        print("Bunday ID raqamdagi kitob topilmadi.")

while True:
    print("\n=== KUTUBXONA TIZIMI ===")
    print("1. Mavjud kitoblarni ko'rish")
    print("2. Kitobni band qilish")
    print("3. Kitobni qaytarish")
    print("4. Chiqish")
    
    tanlov = input("Amr raqamini tanlang (1-4): ")
    
    if tanlov == '1':
        mavjud_kitoblar()
    elif tanlov == '2':
        kitob_band_qilish()
    elif tanlov == '3':
        kitob_qaytarish()
    elif tanlov == '4':
        print("Dastur yakunlandi.")
        break
    else:
        print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

db.close()
