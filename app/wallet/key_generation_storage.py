from utils.env_management import store_key_env
from web3 import Web3
import os

InfuraProvider = os.getenv("INFURA_MAINNET")

w3 = Web3(Web3.HTTPProvider(InfuraProvider))



#If there is no private key, create it (For New Users)
def generate_store_keys():
    print("1")
    if os.getenv("PRIVATE_KEY") is None:
        acc = w3.eth.account.create()
        private_key_gen = w3.to_hex(acc.key)
        account = acc.address
        print(account)
        store_key_env("PRIVATE_KEY",private_key_gen)
        store_key_env("ACCOUNT",account)
