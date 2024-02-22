import requests

def get_ethereum_price_history(days='7', interval='daily'):
    url = f'https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=eur&days={days}&interval={interval}'
    response = requests.get(url)
    price_data = response.json()['prices']
    return price_data

get_ethereum_price_history()