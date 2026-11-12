from customer import Customer
from database import db

while True:
    print("""
    ===== MINI CRM =====

    1. Mijoz qo'shish
    2. Mijozlar ro'yxati
    3. Mijozni ID orqali qidirish
    4. Mijozni yangilash
    5. Mijozni o'chirish
    0. Chiqish
    """)

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        ism = input("Ism: ")
        telefon = input("Telefon: ")
        email = input("Email: ")
        kompaniya = input("Kompaniya: ")

        mijoz = Customer(ism, telefon, email, kompaniya)
        mijoz.qoshish()

    elif tanlov == "2":
        Customer.royxat()

    elif tanlov == "3":
        id = int(input("Mijoz ID sini kiriting: "))
        Customer.qidirish(id)

    elif tanlov == "4":
        id = int(input("Mijoz ID sini kiriting: "))
        ism = input("Yangi ism: ")
        telefon = input("Yangi telefon: ")
        email = input("Yangi email: ")
        kompaniya = input("Yangi kompaniya: ")

        Customer.yangilash(id, ism, telefon, email, kompaniya)

    elif tanlov == "5":
        id = int(input("O'chiriladigan mijoz ID sini kiriting: "))
        Customer.ochirish(id)

    elif tanlov == "0":
        print("Dastur tugadi!")
        db.close()
        break

    else:
        print("Noto'g'ri tanlov!")