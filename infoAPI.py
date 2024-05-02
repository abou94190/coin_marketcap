import requests


def get_api_key_info(api_key):
    url = "https://pro-api.coinmarketcap.com/v1/key/info"
    parameters = {
        "CMC_PRO_API_KEY": '34da595a-6f7a-4582-b18e-86508b7aaa94'
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
    api_key = input("Entrer votre clé API CoinMarketCap: ")
    api_key_info = get_api_key_info(api_key)
    if api_key_info:
        print(api_key_info)


if __name__ == "__main__":
    main()
