
import requests

shahar = input("Shahar nomini kiriting: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={shahar}&count=1&language=uz&format=json"

javob = requests.get(url)
data = javob.json()

if data.get("results"):
    joy = data["results"][0]

    latitude = joy["latitude"]
    longitude = joy["longitude"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

    javob = requests.get(url)
    ob_havo = javob.json()["current"]

    print("\n--- OB-HAVO MA'LUMOTLARI ---")
    print(f"Shahar: {joy['name']}")
    print(f"Harorat: {ob_havo['temperature_2m']} °C")
    print(f"Namlik: {ob_havo['relative_humidity_2m']} %")
    print(f"Shamol tezligi: {ob_havo['wind_speed_10m']} km/soat")

else:
    print("Bunday shahar topilmadi!")
