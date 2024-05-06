import requests
from dotenv import load_dotenv


def get_exchange_assets(exchange_id):
    url = f"https://pro-api.coinmarketcap.com/v1/exchange/assets?id={exchange_id}"
    parameters = {
        "CMC_PRO_API_KEY": "34da595a-6f7a-4582-b18e-86508b7aaa94"
    }

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()  # Raises an exception
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None


def main():
    exchange_id = input("Enter the exchange ID: ")
    exchange_assets = get_exchange_assets(exchange_id)
    if exchange_assets:
        print(exchange_assets)


if __name__ == "__main__":
    main()
