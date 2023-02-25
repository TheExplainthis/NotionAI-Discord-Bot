from threading import Thread
from flask import Flask

app = Flask('NotionAI-Discord-Bot')


@app.route('/')
def home():
    return "Hello World"


def server_run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=server_run)
    t.start()
