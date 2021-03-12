from pycoingecko import CoinGeckoAPI
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from decouple import config

TOKEN = config('API_TELEGRAM_TOKEN')
GROUP_ID = config('GROUP_ID')

bot = Bot(TOKEN)
updater = Updater(TOKEN)
cg = CoinGeckoAPI()

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


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!, My name is Mumu coin-sniffing, type /help to understand me better')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("""
    /help - Returno commands.
/start - Start and presentation.
/coin <symbol> - Returns the value of the entered currency.
    """)


def coin(update: Update, context: CallbackContext) -> None:
    """Send a requested coin value when the command /coin <symbol> is issued."""
    try:
        coin = context.args[0]
        coin_result = coin_value(coin)
        if coin_result == '{}':
            update.message.reply_text('Coin not found')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /coin <symbol>')




def main():
    """Start the bot."""
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("coin", coin))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
