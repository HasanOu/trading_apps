from flask import Flask, render_template, request
import config, json
import sys

app = Flask(__name__)

@app.route('/')

@app.route('/webhook', methods=['POST'])
def webhook():

    webhook_message = request.data
    my_json = webhook_message.decode('utf8').replace("'", '"')
    webhook_message = json.loads(my_json)

    return str(webhook_message)