import argparse
import requests

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from bot.logging_config import setup_logger

from binance.exceptions import (
    BinanceAPIException
)


setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()

try:

    side = validate_side(
        args.side
    )

    order_type = validate_order_type(
        args.type
    )

    quantity = validate_quantity(
        args.quantity
    )

    if (
        order_type == "LIMIT"
        and args.price is None
    ):
        raise ValueError(
            "LIMIT order requires price"
        )

    print("\n===== ORDER SUMMARY =====")

    print(
        f"Symbol: {args.symbol}"
    )

    print(
        f"Side: {side}"
    )

    print(
        f"Type: {order_type}"
    )

    print(
        f"Quantity: {quantity}"
    )

    client = get_client()

    response = place_order(
        client,
        args.symbol.upper(),
        side,
        order_type,
        quantity,
        args.price
    )

    print("\n===== RESPONSE =====")

    print(
        f"Order ID: {response.get('orderId')}"
    )

    print(
        f"Status: {response.get('status')}"
    )

    print(
        f"Executed Qty: {response.get('executedQty')}"
    )

    print(
        f"Avg Price: {response.get('avgPrice')}"
    )

    print(
        "\n✓ Order Successful"
    )
except BinanceAPIException as e:

    print(
        f"\n✗ Binance Error: {e}"
    )

except requests.exceptions.ConnectionError:

    print(
        "\n✗ Network connection failed"
    )

except requests.exceptions.Timeout:

    print(
        "\n✗ Request timed out"
    )

except Exception as e:

    print(
        f"\n✗ Error: {e}"
    )