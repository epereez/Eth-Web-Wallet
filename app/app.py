from flask import Flask, render_template
from wallet.get_balance import get_ethbalance
from wallet.key_generation_storage import generate_store_keys
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',Balance=get_ethbalance(os.getenv("ACCOUNT")))

if __name__ == '__main__':
    generate_store_keys()
    app.run(debug=True)

