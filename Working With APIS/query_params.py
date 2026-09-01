import requests 

url = "https://reqres.in/api/users"
params = {"page": 2}

response = requests.get(url, params=params)
print("Final URL:", response.url) # shows ?page=2

response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)



data = response.json()
print("Page:", data["page"])
for user in data["data"]:
    print(user["email"])