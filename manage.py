import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.environ.get('TOKEN', 'TOKEN')
PORT = int(os.environ.get('PORT', '5000'))


def echo(bot, update):
    update.message.reply_text('Bot answer: ' + update.message.text)


updater = Updater(TOKEN)

# add handlers
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://telegrambotexample31337.herokuapp.com/" + TOKEN)
updater.idle()
