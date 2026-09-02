import requests
import json
from API_KEY import APIKEY

#url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = APIKEY

print("===============================================")
print("      Welcome to the Weather Dashboard!        ")
print("===============================================")

Location = input("Enter a location: ").capitalize()
print(f"Fetching weather data for {Location}...")

response = requests.get(BASE_URL, params={"q": Location, "appid": API_KEY})

data = response.json()

print("===============================================")
print("     Weather Data Retrieved Successfully!      ")
print("===============================================")
print("===============================================")
print(f"          {Location} WEATHER DASHBOARD         ")
print("===============================================")



print(f"Description in {Location}: {data['weather'][0]['description']}")
print(f"Temperature in {Location}: {data['main']['temp']}K")
print(f"Humidity in {Location}: {data['main']['humidity']}%")
print(f"Wind Speed in {Location}: {data['wind']['speed']} m/s")
print(f"Feels Like in {Location}: {data['main']['feels_like']}K")
print(f"Condition in {Location}: {data['weather'][0]['main']}")

history = []
history.append(data)

with open("Weather Dashboard Project/search_history.json", "w") as file:
    json.dump(history, file, indent=4)