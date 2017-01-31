import os
from telegram.ext import Updater
from flask import Flask

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN', 'TOKEN')
# gunicorn default port is 8000
PORT = int(os.environ.get('PORT', '8000'))
updater = Updater(TOKEN)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://telegrambotexample31337.herokuapp.com/" + TOKEN)
print(PORT, TOKEN)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/{0}/".format(TOKEN))
def hello():
    return "hop hay lalalay!"


if __name__ == "__main__":
    app.run()
