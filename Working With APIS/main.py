import requests 

url = "https://jsonplaceholder.typicode.com/posts/1"


response = requests.get(url)

print("Status code:", response.status_code)
print("Content type:", response.headers.get('Content-Type'))

data = response.json()
print("Post title:", data['title'])
print("All data:", data)