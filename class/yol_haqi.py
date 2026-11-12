class Delivery:
    def __init__(self,Ogirlik,Masofa):
        self.ogirlik=Ogirlik
        self.Masofa=Masofa
    def Hisoblagich(self):
        print(f"Masofa: {self.Masofa} bir kilagram ogirlik uchun 1000 som")
        print(f"Ogirlik: {self.ogirlik} bir km uchun 2000 som")
        print(f"Yetkazib berish narxi: {self.ogirlik*1000+self.Masofa*2000}")

t1=Delivery(2,3)

t1.Hisoblagich()