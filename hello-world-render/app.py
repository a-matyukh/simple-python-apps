from module import summa

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, мой друг прекраснйы {summa(1, 2)}!'