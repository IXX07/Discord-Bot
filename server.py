from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route("/")
def hello():
  return "Discord Bot: Mualuenie is still alive"


def run():
  app.run(host='0.0.0.0')


def stay_alive():
  t = Thread(target=run)
  t.start()
