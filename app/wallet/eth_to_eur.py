from wallet.get_eth_info import get_ethprice
from wallet.get_ethbalance import get_eth_balance
import os


#CONVERT USERS ACCOUNT ETHEREUM BALANCE INTO EUR

def convert_eth_eur():
    balance = get_eth_balance(os.getenv("ACCOUNT"))
    eth_price = get_ethprice()
    balance_in_eur = balance*eth_price
    round_balance = round(balance_in_eur,2)
    return round_balance