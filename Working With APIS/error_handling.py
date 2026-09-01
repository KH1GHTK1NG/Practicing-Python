import requests 

try:
    #httpbin /delay/3 waits 3 seconds before responding
    response = requests.get("https://httpbin.org/delay/3", timeout=2)
    response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
    print("Response received:", response.json())
except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")