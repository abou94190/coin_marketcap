import requests


def get_global_metrics(metrics):
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"
    parameters = {
        "convert": "BTC",
        "CMC_PRO_API_KEY": "34da595a-6f7a-4582-b18e-86508b7aaa94"
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


if __name__ == "__main__":
    main()