from src.func_bot import Func_bot
from telegram import Update, Bot, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
import yaml

with open('categories.yaml') as file:
    documents = yaml.full_load(file)

class Commands():
    def start_command(update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text(documents['startText'], parse_mode=ParseMode.MARKDOWN)


    def help_command(update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        update.message.reply_text(documents['helpText'], parse_mode=ParseMode.MARKDOWN)


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
        """Send a requested coin value when the command /set <symbol> <final price> issued."""
        try:
            coin = context.args[0]
            initial_price = context.args[1]

            if 'k' in initial_price.lower():
                initial_price = initial_price.replace('k', '000')
            
            if ',' in initial_price.lower():
                initial_price = initial_price.replace(',', '.')

            update.message.reply_text('Set Value the with Success')
            set_bg_call = Func_bot()
            set_bg_call.awaits_value_backgroud(coin, initial_price)
        except (IndexError, ValueError):
            update.message.reply_text('Usage: /set <symbol> <final price>')


    def cron_command(update: Update, context: CallbackContext) -> None:
        """Send a requested coin value when the command /set <symbol> <initial price> <final price> issued."""
        try:
            coin = context.args[0]
        except:
            update.message.reply_text('Usage: /coin <symbol>', parse_mode=ParseMode.MARKDOWN)
        
        update.message.reply_text('Set Value the with Success')
        set_bg_call = Func_bot()
        set_bg_call.add_coin_in_cron(coin)


    def trending_command(update: Update, context: CallbackContext) -> None:
        """Send a requested coin value when the command /trending is issued."""
        try:
            func_bot = Func_bot()
            trending_coins_result = func_bot.trending_value()
        except (IndexError, ValueError):
            update.message.reply_text('Error when get trending coins.', parse_mode=ParseMode.MARKDOWN)


    def delcron_command(update: Update, context: CallbackContext) -> None:
        """Send a requested coin value when the command /set <symbol> <initial price> <final price> issued."""
        coin = context.args[0]

        update.message.reply_text('Delete Value the with Success')
        set_bg_call = Func_bot()
        set_bg_call.delete_thread(coin)
        update.message.reply_text('Usage: /delcron <symbol> or Cron not Exists', parse_mode=ParseMode.MARKDOWN)