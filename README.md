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

## Note

The application was developed against Binance Futures Testnet APIs.

Input validation, logging, order construction, and API integration were fully implemented.

During testing, Binance Futures Testnet returned:

APIError(code=-1109): Invalid account

despite valid API credentials and successful authentication format checks. This appears related to the Binance Testnet account/environment configuration rather than application logic.