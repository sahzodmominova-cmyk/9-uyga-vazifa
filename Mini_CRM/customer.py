from database import db, cursor

class Customer:

    def __init__(self, ism, telefon, email, kompaniya):
        self.ism = ism
        self.telefon = telefon
        self.email = email
        self.kompaniya = kompaniya

    def qoshish(self):
        cursor.execute("""
        INSERT INTO customers (ism, telefon, email, kompaniya)
        VALUES (?, ?, ?, ?)
        """, (self.ism, self.telefon, self.email, self.kompaniya))

        db.commit()
        print("Mijoz muvaffaqiyatli qo'shildi!")

    @staticmethod
    def royxat():
        cursor.execute("SELECT * FROM customers")
        mijozlar = cursor.fetchall()

        for mijoz in mijozlar:
            print(mijoz)

    @staticmethod
    def qidirish(id):
        cursor.execute("SELECT * FROM customers WHERE id = ?", (id,))
        mijoz = cursor.fetchone()

        if mijoz:
            print(mijoz)
        else:
            print("Mijoz topilmadi!")

    @staticmethod
    def yangilash(id, ism, telefon, email, kompaniya):
        cursor.execute("""
        UPDATE customers
        SET ism = ?, telefon = ?, email = ?, kompaniya = ?
        WHERE id = ?
        """, (ism, telefon, email, kompaniya, id))

        db.commit()

        if cursor.rowcount > 0:
            print("Mijoz ma'lumotlari yangilandi!")
        else:
            print("Mijoz topilmadi!")

    @staticmethod
    def ochirish(id):
        cursor.execute("DELETE FROM customers WHERE id = ?", (id,))
        db.commit()

        if cursor.rowcount > 0:
            print("Mijoz o'chirildi!")
        else:
            print("Mijoz topilmadi!")