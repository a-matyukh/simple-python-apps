from module import get_random_anekdot

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return get_random_anekdot()