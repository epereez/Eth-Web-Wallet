from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to Infura Hosted Node(Apikey stored in .env for extra security)
InfuraProvider = os.getenv("INFURA_PROVIDER")

w3 = Web3(Web3.HTTPProvider(InfuraProvider))



#Function to store anything into .env
def store_key_env(keyName,key):
    envFilePath = ".env"

    with open(envFilePath, "r") as file:
        lines = file.readlines()

    updatedLines = []
    keyFound = False

    for line in lines:
        if line.startswith(keyName+"="):
            updatedLines.append(f"{keyName}={key}\n")
            keyFound = True
        else:
            updatedLines.append(line)

    if not keyFound:
        updatedLines.append(f"{keyName}={key}\n")

    with open(envFilePath,"w") as file:
        file.writelines(updatedLines)

#If there is no private key, create it (For New Users)
if os.getenv("PRIVATE_KEY") is None:
    acc = w3.eth.account.create()
    private_key_gen = w3.to_hex(acc.key)
    account = acc.address
    store_key_env("PRIVATE_KEY",private_key_gen)
    store_key_env("ACCOUNT",account)


#TRANSACTIONS

"""def makeTransaction(recipientAddress,)


transaction = {
    'to': recipientAddress,
    'value': 1000000000,
    'gas': 2000000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
    'nonce': 0,
    'chainId': 1,
    'type': '0x2',  # the type is optional and, if omitted, will be interpreted based on the provided transaction parameters
    'accessList': (  # accessList is optional for dynamic fee transactions
        {
            'address': '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae',
            'storageKeys': (
                '0x0000000000000000000000000000000000000000000000000000000000000003',
                '0x0000000000000000000000000000000000000000000000000000000000000007',
            )
        },
        {
            'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
            'storageKeys': ()
        },
    )
}"""

#SOURCES
#https://web3py.readthedocs.io/en/stable/web3.eth.account.html#eth-account
#https://docs.infura.io/api/
