import requests


def get_global_metrics():
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"
    parameters = {
        "convert": "BTC",
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

# Exemple d'utilisation :


global_metrics = get_global_metrics()
if global_metrics:
    print(global_metrics)