from flask import Flask
import config
import Route

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hooooooooooooooooi'


@app.route('/help')
def help():
    return config.help_string


@app.route('/find')
def find():
    return 'find()'


@app.route('/find/hint')
def find_hint():
    return config.find_hint


@app.route('/get')
def get():
    return 'get()'


@app.route('/get/hint')
def get_hint():
    return config.get_hint