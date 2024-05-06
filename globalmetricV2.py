import requests
import json
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()


def get_global_metrics(metrics):
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"
    parameters = {
        "convert": "BTC",
        "CMC_PRO_API_KEY": os.getenv("CMC_PRO_API_KEY")
    }

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()  # Raises an exception
        data = response.json()

        if metrics == "all":
            return data
        elif metrics in data["data"]:
            return data["data"][metrics]
        else:
            print("commande .")
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None


def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    possible_metrics = [
        "all",
        "active_cryptocurrencies",
        "total_cryptocurrencies",
        "active_market_pairs",
        "total_market_pairs",
        "total_volume_24h",
        "total_volume_24h_reported",
        "altcoin_volume_24h",
        "altcoin_volume_24h_reported",
        "altcoin_market_cap",
        "last_updated"
    ]
    print("Toute les métriques possibles:")
    for metric in possible_metrics:
        print(metric)

    metrics_choice = input("Entrer la métriques souhaitée: ")
    global_metrics = get_global_metrics(metrics_choice)
    if global_metrics:
        print(global_metrics)
        save_data_to_file(global_metrics, 'global_metrics.json')
        print("Data saved to global_metrics.json")


if __name__ == "__main__":
    main()