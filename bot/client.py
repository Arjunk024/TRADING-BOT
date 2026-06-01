from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")
print("KEY FOUND:", API_KEY is not None)
print("SECRET FOUND:", API_SECRET is not None)

def get_client():

    client = Client(
        API_KEY,
        API_SECRET
    )

    client.FUTURES_URL = (
        "https://testnet.binancefuture.com/fapi"
    )

    return client