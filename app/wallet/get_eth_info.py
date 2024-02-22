import os, requests
from decimal import Decimal
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
eth_symbol="ETH"

API_KEY="f3176356-a135-4c0b-8c8e-6bf2287f35c2"
#API_KEY=os.getenv("COINMARKETCAP_APIKEY")

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}

parameters = {
    "symbol": eth_symbol,
    "convert": "EUR",
}

def get_ethprice():
    try:
        response = requests.get(url, headers=headers, params=parameters)
        response_json = response.json()
        eth_price = response_json['data'][eth_symbol]['quote']['EUR']['price']
        eth_price_decimal = Decimal(str(eth_price))
        return eth_price_decimal

    except KeyError as e:
        print(f"Key error encountered: {e}. Check the JSON path.")
    except Exception as e:
        print(f"Couldn't retrieve Ethereum price: {e}")

def get_24h_change():
    response = requests.get(url, headers=headers, params=parameters)
    response_json = response.json()
    change24h = response_json['data'][eth_symbol]['quote']['EUR']['percent_change_24h']
    return change24h
def get_7d_change():
    response = requests.get(url, headers=headers, params=parameters)
    response_json = response.json()
    change7d = response_json['data'][eth_symbol]['quote']['EUR']['percent_change_7d']
    return change7d
def get_30d_change():
    response = requests.get(url, headers=headers, params=parameters)
    response_json = response.json()
    change30d = response_json['data'][eth_symbol]['quote']['EUR']['percent_change_30d']
    return change30d

get_ethprice()