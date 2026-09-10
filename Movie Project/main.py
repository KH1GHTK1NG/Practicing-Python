import requests
import json

BASE_URL = "https://www.omdbapi.com/"
API_KEY = "dfaa10b5"

Movie = input("Enter the movie: ")

response = requests.get(BASE_URL, params={"s": Movie, "apikey": API_KEY})



data = response.json()

for movie in data['Search']:
    print(f"Title: {movie['Title']}") # I want to get every instance of the title in the search results, not just the first one
    print(f"Year: {movie['Year']}")
    print(f"IMDB ID: {movie['imdbID']}")
    print(f"Type: {movie['Type']}")
    print(f"Genre: {movie.get('Genre', 'N/A')}") # Genre is not always available in the search results, so we use .get() to avoid KeyError
    print(f"Rating: {movie.get('imdbRating', 'N/A')}") # Rating is not always available in the search results, so we use .get() to avoid KeyError
    print(f"Plot: {movie.get('Plot', 'N/A')}") # Plot is not always available in the search results, so we use .get() to avoid KeyError
    print(f"Director: {movie.get('Director', 'N/A')}") # Director is not always available in the search results, so we use .get() to avoid KeyError
    print("-" * 30)