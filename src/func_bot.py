import config.configs as config
import json
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
            self.send_message(f'*{id.title()}* está com o valor de ${result[id]["usd"]:,.4f}')
        except:
            result = '{}'
        return result


    def check_backgroud_coin(self, symbol):
        """Call the send_message function to send the coin value and return coin value"""
        #print(symbol)
        id = [c for c in self.list_coins() if c['symbol'] == symbol.lower()][0]['id']
        result = config.cg.get_price(ids=id, vs_currencies='usd')
        result = result[id]['usd']
        #print(result)
        return result

    def return_id_to_symbol(self, symbol):
        id = [c for c in self.list_coins() if c['symbol'] == symbol.lower()][0]['id']
        return id


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
        config.bot.send_message(config.GROUP_ID, text=msg, parse_mode=ParseMode.MARKDOWN)


    def is_correct_response(self, response):
        """Check that the response returned 'success'"""
        return float(response) > float(self.valueb)

    def my_poll(self):
        polling.poll(
            lambda: self.check_backgroud_coin(self.idb),
            check_success=self.is_correct_response,
            step=1,
            poll_forever=True
        )
        coin = [c for c in self.list_coins() if c['symbol'] == self.idb.lower()][0]['id']
        
        self.send_message(f"O valor da moeda {coin.title()} atingiu o alvo de ${float(self.valueb):,.4f}!!")
        self.coin_value(self.idb)


    def awaits_value_backgroud(self, id, value):
        self.idb = id
        self.valueb = value
        #print(f'Set Value the with Success {id} {value}' )
        awaiting_value = threading.Thread(target=self.my_poll)
        awaiting_value.start()


    def cron_json_send(self):
        result, fl = self.read_json()


    def polling_cron(self):
        polling.poll(
            lambda: self.send_message_cron_bg(),
            step=60*60,
            poll_forever=True
        )

    
    def read_json(self):
        fl = open("thread_cron_file.json", "r+")
        data = json.load(fl)

        return data, fl


    def add_coin_in_cron(self, symbol):
        data, fl = self.read_json()
        id = self.return_id_to_symbol(symbol)
        list_ids = [i['id'] for i in data['threads']]
        
        if id in list_ids:
            self.send_message('Essa moeda já existe no cron. Agora é só aguardar!')
        else:
            dtc = {'symbol': symbol, 'id': id}
            data['threads'].append(dtc)

            fl.seek(0)
            json.dump(data, fl)
        
   
    def delete_thread(self, symbol):
        data = self.read_json()[0]    

        res = list(filter(lambda i: i['symbol'] != symbol, data['threads']))
        data['threads'] = res
        
        with open("thread_cron_file.json", "w") as fl:
            json.dump(data, fl)


    def send_message_cron_bg(self):
        data, fl = self.read_json()
        coins = [self.coin_value(coin['symbol']) for coin in data['threads']]


    def threads_cron_bg(self):
        print('Subiu o Cron')
        bg_cron = threading.Thread(target=self.polling_cron)
        bg_cron.start()