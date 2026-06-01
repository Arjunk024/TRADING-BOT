from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_SECRET_KEY")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    print(client.futures_account_balance())
except Exception as e:
    print(e)