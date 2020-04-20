#!/usr/bin/python3
'''
Module: Basic Flask functionality
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    '''
    rtype: str
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def displayHBNB():
    '''
    rtype: str
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    '''
    rtype: str
    '''
    return text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
