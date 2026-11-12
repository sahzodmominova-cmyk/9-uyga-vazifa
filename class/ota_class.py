class Report:
    def __init__(self):
        pass
    def generate(self):
        print("Hisobot tayotlan moqda")

class PDFReport(Report):
    def generate(self):
        print(f"pdf yaratilmoqda")
class ExcelReport(Report):
    def generate(self):
        print(f"exsle farmat yaratilmoqda")
class HTMLReport(Report):
    def generate(self):
        print(f"html yaratilmoqda")

t=Report()
t.generate()
t1=PDFReport()
t1.generate()
t2=ExcelReport()
t2.generate()
t3=HTMLReport()
t3.generate()