import requests

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

response = requests.get(url, timeout=10)
sorov=input("Valyutani kiriting: ")
if response.status_code == 200:
    data = response.json()
    for valyuta in data:
        if sorov.lower()==valyuta["Ccy"].lower():
            print(valyuta["Ccy"], "-", valyuta["CcyNm_UZ"], ":", valyuta["Rate"], "so'm")
            break
    else:
        print("Bunday valyuta topilmadi")
else:
    print("Xatolik:", response.status_code)
