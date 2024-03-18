import os  
from dotenv import load_dotenv  
from web3 import Web3, exceptions  
  
load_dotenv()  
  
private_key = os.getenv('PRIVATE_KEY')   
INFURA_KEY = os.getenv("INFURA_KEY")
w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_KEY}"))

def makeTransaction(from_account, to_account):
    try:  
        from_account = w3.to_checksum_address(from_account)  
    except exceptions.InvalidAddress:  
        print(f"Invalid 'from_account' address: {from_account}")  
    
    try:  
        to_account = w3.to_checksum_address(to_account)  
    except exceptions.InvalidAddress:  
        print(f"Invalid 'to_account' address: {to_account}")  
    
    nonce = w3.eth.get_transaction_count(from_account)  
    tx = {
        'type': '0x2',
        'nonce': nonce,
        'from': from_account,
        'to': to_account,
        'value': w3.to_wei(0.01, 'ether'),
        'maxFeePerGas': w3.to_wei('250', 'gwei'),
        'maxPriorityFeePerGas': w3.to_wei('3', 'gwei'),
        'chainId': 11155111
    }
    gas = w3.eth.estimate_gas(tx)
    tx['gas'] = gas
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction hash: " + str(w3.to_hex(tx_hash)))