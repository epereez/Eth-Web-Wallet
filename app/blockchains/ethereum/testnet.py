from web3 import Web3
import os

INFURA_KEY = os.getenv("INFURA_KEY")
w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_KEY}"))
address = os.getenv("ACCOUNT")
private_key = os.getenv('PRIVATE_KEY')  

def transaction(recipient_address, amount):
    nonce = w3.eth.getTransactionCount(address)

    transaction = {
        'to': recipient_address,
        'value': w3.toWei(amount, 'ether'),  # Amount of ETH to send
        'gas': 21000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': nonce,
        'chainId': 11155420  # Sepolia's chain ID
    }

    # Sign the transaction
    signed_tx = w3.eth.account.signTransaction(transaction, private_key)

    # Send the transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Get the transaction hash
    print("Transaction hash:", w3.toHex(tx_hash))
