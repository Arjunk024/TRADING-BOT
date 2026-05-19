import argparse
import logging
import os

from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

client = Client(API_KEY, API_SECRET)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    params = {
        "symbol": args.symbol.upper(),
        "side": args.side.upper(),
        "type": args.type.upper(),
        "quantity": args.quantity
    }

    if args.type.upper() == "LIMIT":
        params["price"] = args.price
        params["timeInForce"] = "GTC"

    logger.info(f"Request: {params}")

    response = client.futures_create_order(**params)

    logger.info(f"Response: {response}")

    print("\nORDER SUCCESSFUL")
    print(response)

except BinanceAPIException as e:

    logger.error(str(e))

    print("\nORDER FAILED")
    print(e)

except Exception as e:

    logger.error(str(e))

    print("\nERROR")
    print(e)