class ElectricMeter:
    def __init__(self,egasi,oldingi,hozirgi):
        self.egasi=egasi
        self.oldingi=oldingi
        self.hozirgi=hozirgi

    def miqdor(self):
        print(f"Egasi ismi: {self.egasi}\nsariblangan energiya {self.hozirgi-self.oldingi} kw")

t=ElectricMeter("Biloljon",1455,1888)
t.miqdor()
