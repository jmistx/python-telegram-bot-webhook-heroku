import os
import telegram
from telegram.ext import Updater, CommandHandler
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN', 'TOKEN')
PORT = int(os.environ.get('PORT', '8000'))
print('Data', PORT, TOKEN)

bot = telegram.Bot(token=TOKEN)
bot.set_webhook(webhook_url="https://telegrambotexample31337.herokuapp.com/" + TOKEN)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/{0}/".format(TOKEN))
def dispatch():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'




if __name__ == "__main__":
    app.run()
