import os
import telegram
import json
from telegram.ext import Updater, CommandHandler
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN', 'TOKEN')
PORT = int(os.environ.get('PORT', '8000'))
print('Data', PORT, TOKEN)

global bot
bot = telegram.Bot(token=TOKEN)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/{0}/".format(TOKEN), methods=['GET', 'POST'])
def dispatch():
    print('WHAT?!')
    if request.method == "POST":
        data = request.get_json(force=True)
        update = telegram.Update.de_json(data, bot)
        print(dir(update))

        chat_id = update.message.chat.id
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'

@app.route('/set_webhook')
def set_webhook():
    s = bot.set_webhook(webhook_url="https://telegrambotexample31337.herokuapp.com/" + TOKEN)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


if __name__ == "__main__":
    app.run()
