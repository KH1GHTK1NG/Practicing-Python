import json
import requests

class CryptoPriceTracker:
    BASE_URL = "https://api.freecryptoapi.com/v1/getData"
    API_KEY = "m8f4czfunum3s9cmlni3"

    def __init__(self, coin_symbol):
        self.coin_symbol = coin_symbol.upper()
        self.data = None

    def fetch_data(self):
        print("Fetching data...")
        response = requests.get(
            self.BASE_URL,
            headers={"Authorization": f"Bearer {self.API_KEY}"},
            params={"symbol": self.coin_symbol}
        )
        self.data = response.json()

    def save_data_to_file(self, filename="crypto_data.json"):
        with open(filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def display_data(self):
        if not self.data or 'symbols' not in self.data or not self.data['symbols']:
            print(f"No data found for {self.coin_symbol}.")
            return

        coin_data = self.data['symbols'][0]
        print(f"====={self.coin_symbol}=====")
        print(f"Cryptocurrency: {coin_data['symbol']}")
        print(f"Last Price: ${coin_data['last']}")
        print(f"Highest Price: ${coin_data['highest']}")
        print(f"Lowest Price: ${coin_data['lowest']}")


print("===============================================")
print("                CRYPTO TRACKER                 ")
print("===============================================")


coin = input("Enter the cryptocurrency symbol (e.g., BTC, ETH): ").upper()

CryptoTracker = CryptoPriceTracker(coin)
CryptoTracker.fetch_data()
CryptoTracker.display_data()
CryptoTracker.save_data_to_file("Crypto Price Tracker/crypto_data.json")


