from flask import Flask, render_template, request
from wallet.get_ethbalance import get_eth_balance
from wallet.key_generation_storage import generate_store_keys
from wallet.eth_to_eur import convert_eth_eur
from blockchains.ethereum.testnet import transaction
from wallet.get_eth_info import get_24h_change, get_30d_change, get_7d_change
from wallet.eth_price_history import get_ethereum_price_history
from dotenv import load_dotenv
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    generate_store_keys()
    return render_template('home.html',Balance=convert_eth_eur(),Balance_eth=round(get_eth_balance(os.getenv("ACCOUNT")),5))

@app.route('/transactions')
def transactions():
    recieve_popup = os.getenv("ACCOUNT")
    return render_template('transactions.html',Balance=convert_eth_eur(),Balance_eth=round(get_eth_balance(os.getenv("ACCOUNT")),5),recieve_popup=recieve_popup)

@app.route('/view')
def view():
    data = {
        "24h": get_24h_change(),
        "7d": get_7d_change(),
        "30d": get_30d_change(),
    }

    prices = get_ethereum_price_history()

    df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
    df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'], mode='lines+markers', name='ETH Price'))
    fig.update_layout(
    width=940,  # Set the width of the graph
    plot_bgcolor='#070F2B',  # Set the plot background color
    paper_bgcolor='#070F2B',  # Set the overall background color
    font=dict(color='white'),  # Set the font color to white for contrast
    xaxis=dict(showline=True, linewidth=2, linecolor='blue', gridcolor='darkblue'),
    yaxis=dict(showline=True, linewidth=2, linecolor='blue', gridcolor='darkblue'),
    margin=dict(l=0, r=0, t=0, b=0)  # Minimize margin to fit better in center
    )


    graph_html = pio.to_html(fig, full_html=False)
    return render_template('view.html',data=data, graph_html=graph_html)

@app.route('/api/transact', methods=['POST'])
def transact():
    data = request.get_json()
    amount = data['amount']
    recipient_address = data['address']
    return transaction(recipient_address,amount)

if __name__ == '__main__':
    app.run(debug=True)

