import requests


def get_exchange_info(exchange_id):
    url = f"https://pro-api.coinmarketcap.com/v1/exchange/info?id={exchange_id}&aux=urls,logo,description,date_launched,notice"
    parameters = {
        "CMC_PRO_API_KEY": "34da595a-6f7a-4582-b18e-86508b7aaa94"
    }

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()  # Raises an exception
        data = response.json()
        filtered_data = {
            "url": data["data"][str(exchange_id)]["urls"],
            "logo": data["data"][str(exchange_id)]["logo"],
            "description": data["data"][str(exchange_id)]["description"],
            "date_launched": data["data"][str(exchange_id)]["date_launched"],
            "notice": data["data"][str(exchange_id)]["notice"]
        }
        return filtered_data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None


def main():
    exchange_id = input("Enter the exchange ID: ")
    exchange_info = get_exchange_info(exchange_id)
    if exchange_info:
        print(exchange_info)


if __name__ == "__main__":
    main()
