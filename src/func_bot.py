import config.configs as config

class Func_bot():
    def __init__(self):
        pass
    def coin_value(self, symbol):
        """Call the send_message function to send the coin value and return coin value"""
        # try:
        #     id = [c for c in list_coins() if c['symbol'] == symbol.lower()][0]['id']
        #     result = config.cg.get_price(ids=id, vs_currencies='usd')
        #     send_message(f'O valor do {id.title()} está ${result[id]["usd"]:,.4f}')
        # except:
        #     result = '{}'
        # return result

        id = [c for c in self.list_coins() if c['symbol'] == symbol.lower()][0]['id']
        result = config.cg.get_price(ids=id, vs_currencies='usd')
        self.send_message(f'O valor do {id.title()} está ${result[id]["usd"]:,.4f}')
        

    def list_coins(self):
        """List all coins in API"""
        result = config.cg.get_coins_list()
        return result


    def send_message(self, msg) -> None:
        """Send the message forwarded to the function"""
        config.bot.send_message(config.GROUP_ID, text=msg)