import config.configs as config
import json

class Func_bot():
    def __init__(self):
        pass
    def coin_value(self, symbol):
        """Call the send_message function to send the coin value and return coin value"""
        try:
            id = [c for c in self.list_coins() if c['symbol'] == symbol.lower()][0]['id']
            result = config.cg.get_price(ids=id, vs_currencies='usd')
            self.send_message(f'O valor do {id.title()} está ${result[id]["usd"]:,.4f}')
        except:
            result = '{}'
        return result


    def trending_value(self):
        try:
            result = self.list_trending_coins()
            trend_list = [x['item']['name'] for x in result['coins']]

            txt = 'Trending: \n'
            
            for i, item in enumerate(trend_list, start=1):
                txt += f' {i} - {item} \n'

            self.send_message(txt)
        except:
            result = '{}'
        return result


    def list_trending_coins(self):
        """Get top 7 trending coin searches"""
        result = config.cg.get_search_trending()
        return result


    def list_coins(self):
        """List all coins in API"""
        result = config.cg.get_coins_list()
        return result


    def send_message(self, msg) -> None:
        """Send the message forwarded to the function"""
        config.bot.send_message(config.GROUP_ID, text=msg)

