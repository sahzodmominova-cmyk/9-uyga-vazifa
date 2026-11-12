from databases import db, cursor


def xarajat_qoshish():
    kategoriya = input("Kategoriyani kiriting: ")
    summa = float(input("Summani kiriting: "))
    sana = input("Sanani kiriting: ")

    cursor.execute("""
        INSERT INTO xarajatlar (kategoriya, summa, sana)
        VALUES (?, ?, ?)
    """, (kategoriya, summa, sana))

    db.commit()
    print("Xarajat qoshildi!")


def barcha_xarajatlar():
    cursor.execute("SELECT * FROM xarajatlar")
    xarajatlar = cursor.fetchall()

    if not xarajatlar:
        print("Xarajatlar mavjud emas!")
        return

    for xarajat in xarajatlar:
        print(xarajat)


def kategoriya_hisoblash():
    kategoriya = input("Kategoriyani kiriting: ")

    cursor.execute("""
        SELECT SUM(summa) FROM xarajatlar
        WHERE kategoriya = ?
    """, (kategoriya,))

    natija = cursor.fetchone()[0]

    if natija is None:
        natija = 0

    print(f"{kategoriya} boyicha jami xarajat: {natija} som")


def xarajat_ochirish():
    id = int(input("Ochiriladigan xarajat ID sini kiriting: "))

    cursor.execute("DELETE FROM xarajatlar WHERE id = ?", (id,))
    db.commit()

    if cursor.rowcount > 0:
        print("Xarajat ochirildi!")
    else:
        print("Bunday ID mavjud emas!")


while True:
    print("===== XARAJATLAR NAZORATI =====")
    print("1. Xarajat qoshish")
    print("2. Barcha xarajatlarni korish")
    print("3. Kategoriya boyicha hisoblash")
    print("4. Xarajatni ochirish")
    print("5. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        xarajat_qoshish()

    elif tanlov == "2":
        barcha_xarajatlar()

    elif tanlov == "3":
        kategoriya_hisoblash()

    elif tanlov == "4":
        xarajat_ochirish()

    elif tanlov == "5":
        print("Dastur tugadi!")
        db.close()
        break

    else:
        print("Notogri tanlov!")