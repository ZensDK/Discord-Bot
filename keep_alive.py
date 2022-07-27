from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return """
  Github.com/ZensDK
  If you'd like to find a free host you can use | https://uptimerobot.com/
  """

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
