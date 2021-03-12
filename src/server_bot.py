import config.configs as config

from src.commands_bot import Commands
from telegram.ext import Updater, CommandHandler, CallbackContext

class Server():
    def main(self):
        """Start the bot."""
        dispatcher = config.token.dispatcher

        dispatcher.add_handler(CommandHandler("start", Commands.start_command))
        dispatcher.add_handler(CommandHandler("coin", Commands.coin_command))
        dispatcher.add_handler(CommandHandler("help", Commands.help_command))

        # Start the Bot
        config.token.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        config.token.idle()