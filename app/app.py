from flask import Flask, render_template
from wallet.get_ethbalance import get_eth_balance
from wallet.key_generation_storage import generate_store_keys
from wallet.eth_to_eur import convert_eth_eur
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    generate_store_keys()
    return render_template('home.html',Balance=convert_eth_eur(),Balance_eth=round(get_eth_balance(os.getenv("ACCOUNT")),5))

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

if __name__ == '__main__':
    app.run(debug=True)

