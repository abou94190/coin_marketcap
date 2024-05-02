# coin_marketcap

1- globalmetricV2.py :

Ce programme envoie une requête qui permettra de récuperer les métriques
globales de la cryptomonnaie BTC en format json .
Le programme nous propose ensuiste les métriques possible à entrer :
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
En choisir une pour récuperer les informations spécifiques à ce métrique.

2- exchangeasset.py :
Ce programme envoie une requête qui récupére les échanges d'actifs cryptos de parties tiers (entreprise par exemple).
Entrer l'ID de la partie tiers voulue dans le programme . ( rechercher d'abord les ID's sur CoinMarketCap)

3- metadataExchange.py :

Requête qui renvoie toutes les métadonnées statiques disponibles pour une ou plusieurs crypto-monnaies (dans ce cas Ethereum) . 
Ces informations incluent des détails tels que le logo, la description, l'URL du site Web officiel, 
les liens sociaux et les liens vers la documentation technique d'une crypto-monnaie.


4- infoAPI.py :

Ce programme envoie une requête qui renvoie les détails de la clé API et les statstique d'utilisation.
Entrer la clé API utilisé.

5- coinscategory :

Ce programme envoie une requête qui renvoie les détails des catégories de coins cryptos .

