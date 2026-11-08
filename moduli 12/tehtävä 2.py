
import requests

# Oma OpenWeather API-avain
api_key = "d21fe994f6d7dad359b0ff0213717c2e"

# Kysytään käyttäjältä paikkakunta
kaupunki = input("Anna paikkakunnan nimi: ")

# Haetaan säätiedot rajapinnasta
url = "https://api.openweathermap.org/data/2.5/weather"

parametrit = {
    "q": kaupunki,
    "appid": api_key,
    "lang": "fi"
}

vastaus = requests.get(url, params=parametrit)

# Tarkistetaan, onnistuiko haku
if vastaus.status_code == 200:
    data = vastaus.json()

    # Haetaan säätilan kuvaus
    saatila = data["weather"][0]["description"]

    # Haetaan lämpötila Kelvin-asteina
    lampotila_kelvin = data["main"]["temp"]

    # Muutetaan Kelvin Celsius-asteiksi
    lampotila_celsius = lampotila_kelvin - 273.15

    # Tulostetaan säätiedot
    print("Säätila:", saatila)
    print("Lämpötila:", round(lampotila_celsius, 1), "°C")

else:
    print("Tarkista paikkakunta ja API-avain.")
