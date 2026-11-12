from database import db, cursor

cursor.execute("SELECT * FROM mahsulotlar")
mahsulotlar = cursor.fetchall()

son = 0
umumiy_qiymat = 0

for mahsulot in mahsulotlar:
    son += 1

    narx = mahsulot[2]
    miqdor = mahsulot[3]

    umumiy_qiymat += narx * miqdor

print(f"Ombordagi mahsulotlar soni: {son}")
print(f"Umumiy qiymat: {umumiy_qiymat} so'm")

db.close()