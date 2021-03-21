from src.func_bot import Func_bot
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import yaml

with open('categories.yaml') as file:
    documents = yaml.full_load(file)

class Commands():
    def start_command(update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text(documents['startText'])


    def help_command(update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        update.message.reply_text(documents['helpText'])


    def coin_command(update: Update, context: CallbackContext) -> None:
        """Send a requested coin value when the command /coin <symbol> is issued."""
        try:
            coin = context.args[0]
            func_bot = Func_bot()
            coin_result = func_bot.coin_value(coin)
            if coin_result == '{}':
                update.message.reply_text('Coin not found')
        except (IndexError, ValueError):
            update.message.reply_text('Usage: /coin <symbol>')

    
    def set_command(update: Update, context: CallbackContext) -> None:
        """Send a requested coin value when the command /set <symbol> <initial price> <final price> issued."""
        coin = context.args[0]
        initial_price = context.args[1]

        if 'k' in initial_price.lower():
            initial_price = initial_price.replace('k', '000')

        update.message.reply_text('Set Value the with Success')
        set_bg_call = Func_bot()
        set_bg_call.awaits_value_backgroud(coin, initial_price)


    def cron_command(update: Update, context: CallbackContext) -> None:
        """Send a requested coin value when the command /set <symbol> <initial price> <final price> issued."""
        coin = context.args[0]

        update.message.reply_text('Set Value the with Success')
        set_bg_call = Func_bot()
        set_bg_call.awaits_value_backgroud_cron(coin)
