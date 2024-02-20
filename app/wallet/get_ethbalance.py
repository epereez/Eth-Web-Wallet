import httpx, json
from decimal import Decimal

#GET CURRENT ETH BALANCE 

def get_eth_balance(address):
    try:
        response = httpx.get(f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=BUDW5KJUSCX1KH3TW64TJJ36HFZ4RGS1CU")
        response_data = json.loads(response.text)
        balance_wei = response_data["result"]
        balance_ether = Decimal(balance_wei)/Decimal(10**18)
        return balance_ether
    except Exception as e:
        print(f"Couldnt get account balance: {e}")

