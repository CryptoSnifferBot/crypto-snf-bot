import config.configs as config

import threading
import polling

class Func_bot():
    def __init__(self):
        pass


    def coin_value(self, symbol):
        """Call the send_message function to send the coin value and return coin value"""
        try:
            id = [c for c in self.list_coins() if c['symbol'] == symbol.lower()][0]['id']
            result = config.cg.get_price(ids=id, vs_currencies='usd')
            self.send_message(f'The value of {id.title()} is ${result[id]["usd"]:,.4f}')
        except:
            result = '{}'
        return result

    
    def check_backgroud_coin(self, symbol):
        """Call the send_message function to send the coin value and return coin value"""
        print(symbol)
        id = [c for c in self.list_coins() if c['symbol'] == symbol.lower()][0]['id']
        result = config.cg.get_price(ids=id, vs_currencies='usd')
        result = result[id]['usd']
    #   except:
    #         result = '{}'
        print(result)
        return result
        

    def list_coins(self):
        """List all coins in API"""
        result = config.cg.get_coins_list()
        return result


    def send_message(self, msg) -> None:
        """Send the message forwarded to the function"""
        config.bot.send_message(config.GROUP_ID, text=msg)


    def is_correct_response(self, response):
        """Check that the response returned 'success'"""
        coin = list(response.keys())[0]
        return float(response[coin]['usd']) > float(self.valueb)

    def my_poll(self):
        polling.poll(
            lambda: self.check_backgroud_coin(self.idb),
            check_success=self.is_correct_response,
            step=1,
            poll_forever=True
        )
        coin = [c for c in self.list_coins() if c['symbol'] == self.idb.lower()][0]['id']
        
        self.send_message(f"The Value {coin.title()} passed the target of ${float(self.valueb):,.4f}")
        self.coin_value(self.idb)


    def awaits_value_backgroud(self, id, value):
        self.idb = id
        self.valueb = value
        print(f'Set Value the with Success {id} {value}' )
        awaiting_value = threading.Thread(target=self.my_poll)
        awaiting_value.start()


    def my_poll_cron(self):
        coin = [c for c in self.list_coins() if c['symbol'] == self.idbb.lower()][0]['id']
        polling.poll(
            lambda: self.send_message(f"The Value {coin.title()} is ${float(self.check_backgroud_coin(self.idbb)):,.4f}"),
            step=60*60,
            poll_forever=True
        )
        
        self.coin_value(self.idb)

    
    def awaits_value_backgroud_cron(self, id):
        self.idbb = id
        print(f'Successfully scheduled coin {id} ' )
        awaiting_value = threading.Thread(target=self.my_poll_cron)
        awaiting_value.start()



