from pycoingecko import CoinGeckoAPI
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from decouple import config
from src.strings_bot import help_f
from src.server_bot import Server

if __name__ == '__main__':
    TOKEN = config('API_TELEGRAM_TOKEN')
    GROUP_ID = config('GROUP_ID')

    bot = Bot(TOKEN)
    token = Updater(TOKEN)
    cg = CoinGeckoAPI()

    Server(token)
