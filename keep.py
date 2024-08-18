from flask import Flask, render_template,json,request,send_file
from threading import Thread
from datetime import datetime
import os

app = Flask(__name__,template_folder='')


@app.route('/')
def index():
  return 'Hello'
  

def run():
  app.run(debug=False,host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
