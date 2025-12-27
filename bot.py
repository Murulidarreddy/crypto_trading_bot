from binance.client import Client
from config import API_KEY, API_SECRET
from logger import logger

def place_market_order(client, symbol, side, quantity):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )
    logger.info(f"Market order placed: {order}")
    print("✅ Market order placed successfully")
    print("Order ID:", order["orderId"])

def place_limit_order(client, symbol, side, quantity, price):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )
    logger.info(f"Limit order placed: {order}")
    print("✅ Limit order placed successfully")
    print("Order ID:", order["orderId"])

def main():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper().strip()
    side = input("Enter side (BUY / SELL): ").upper().strip()
    order_type = input("Enter order type (MARKET / LIMIT): ").upper().strip()

    try:
        quantity = float(input("Enter quantity: "))
    except ValueError:
        print("❌ Quantity must be a number")
        return

    if side not in ["BUY", "SELL"]:
        print("❌ Side must be BUY or SELL")
        return

    try:
        if order_type == "MARKET":
            place_market_order(client, symbol, side, quantity)

        elif order_type == "LIMIT":
            price = float(input("Enter limit price: "))
            place_limit_order(client, symbol, side, quantity, price)

        else:
            print("❌ Order type must be MARKET or LIMIT")

    except Exception as e:
        logger.error(f"Order failed: {e}")
        print("❌ Error placing order:", e)

if __name__ == "__main__":
    main()
