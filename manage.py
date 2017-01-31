import os
import telegram
from pprint import pprint
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN', 'TOKEN')

global bot
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def hello():
    return 'Hello World!'


# this routing a single really needed, and it can be programmed easly
@app.route('/{0}'.format(TOKEN), methods=['GET', 'POST'])
def dispatch():
    if request.method == 'POST':
        # You probably want to convert json to object with properties
        # See Updater.de_json
        data = request.get_json(force=True)
        chat_id = data['message']['chat']['id']
        text = data['message']['text'].encode('utf-8')

        bot.sendMessage(chat_id=chat_id, text=text)


    return 'ok'


# This routing actually not required. You can setup webhook from any program.
@app.route('/{0}/set_webhook'.format(TOKEN))
def set_webhook():
    s = bot.set_webhook(webhook_url='https://telegrambotexample31337.herokuapp.com/' + TOKEN)
    if s:
        return 'webhook setup ok'
    else:
        return 'webhook setup failed'


if __name__ == '__main__':
    app.run()
