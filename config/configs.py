from pycoingecko import CoinGeckoAPI
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from decouple import config
from src.func_bot import Func_bot
from src.server_bot import Server


TOKEN = config('API_TELEGRAM_TOKEN')
GROUP_ID = config('GROUP_ID')

bot = Bot(TOKEN)
token = Updater(TOKEN)
cg = CoinGeckoAPI()

