# Binance Futures Trading Bot

## Features
- Place MARKET orders
- Place LIMIT orders
- Uses Binance Futures Testnet
- Logs all requests and responses

## Installation

pip install -r requirements.txt

## Run Example

Market Order:

python app.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:

python app.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000