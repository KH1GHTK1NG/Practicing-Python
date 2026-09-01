import requests 

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello from Python",
    "body": "This is a test post created using the requests library in Python.",
    "userId": 1
}

response = requests.post(url, json=payload)
print("Status code:", response.status_code)
data = response.json()
print("Response data:", data)