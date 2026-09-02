import requests

token = "AAAAAAAAAAAIHOBNB OUHBU JJljyiobeoiynweojuiofugihei7geioufhw8yfouruioey89eoe"

BASE_URL = "https://api.x.com/2/users/by/username/TechWithTim"

Readers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(BASE_URL, headers=Readers)

print("Status Code:", response.status_code)
print("URL:", response.url)

try:
    data = response.json()
    print("Data:", data)
except ValueError:
    print("Response content is not valid JSON.")
    print("Response content:", response.text)