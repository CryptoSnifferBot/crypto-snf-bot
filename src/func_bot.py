def coin_value(symbol):
    """Call the send_message function to send the coin value and return coin value"""
    try:
        id = [c for c in list_coins() if c['symbol'] == symbol.lower()][0]['id']
        result = cg.get_price(ids=id, vs_currencies='usd')
        send_message(f'O valor do {id.title()} está ${result[id]["usd"]:,.4f}')
    except:
        result = '{}'
    return result


def list_coins():
    """List all coins in API"""
    result = cg.get_coins_list()
    return result


def send_message(msg) -> None:
    """Send the message forwarded to the function"""
    bot.send_message(GROUP_ID, text=msg)