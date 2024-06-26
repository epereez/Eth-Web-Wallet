import httpx, json, os
from decimal import Decimal
from web3 import Web3

INFURA_KEY = os.getenv("INFURA_KEY")
w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_KEY}"))

#GET CURRENT ETH BALANCE 


#MAINNET
'''def get_eth_balance(address):
    try:
        response = httpx.get(f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=BUDW5KJUSCX1KH3TW64TJJ36HFZ4RGS1CU")
        response_data = json.loads(response.text)
        balance_wei = response_data["result"]
        balance_ether = Decimal(balance_wei)/Decimal(10**18)
        return balance_ether
    except Exception as e:
        print(f"Couldnt get account balance: {e}")

'''

#TESTNET

def get_eth_balance(address):
    if not w3.is_connected():
        print("Failed to connect to the Ethereum network")
        return
    checksum_address = w3.to_checksum_address("0xd2004187aea91c9bf85b39eee12a2ab562656632")
    balance_wei = w3.eth.get_balance(checksum_address)
    balance_ether = Decimal(balance_wei/10**18)
    return balance_ether

