import config.configs as config
from src.func_bot import Func_bot
from src.commands_bot import Commands
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
import json

class Server():
    def main(self):
        """Start the bot."""
        dispatcher = config.token.dispatcher

        dispatcher.add_handler(CommandHandler("start", Commands.start_command))
        dispatcher.add_handler(CommandHandler("coin", Commands.coin_command))
        dispatcher.add_handler(CommandHandler("trending", Commands.trending_command))
        dispatcher.add_handler(CommandHandler("help", Commands.help_command))
        dispatcher.add_handler(CommandHandler("set", Commands.set_command))
        dispatcher.add_handler(CommandHandler("cron", Commands.cron_command))
        dispatcher.add_handler(CommandHandler("delcron", Commands.delcron_command))

        if not os.path.exists('thread_cron_file.json'):
            with open("thread_cron_file.json", "w") as fl:
                dtc = {"threads": []}
                json.dump(dtc, fl)

        polling_cron = Func_bot()
        polling_cron.threads_cron_bg()

        # Start the Bot
        print('Server Subiu')
        config.token.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        config.token.idle()