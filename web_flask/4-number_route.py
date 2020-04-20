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


@app.route("/python/<text>", strict_slashes=False)
def pythonText(text):
    '''
    rtype: str
    '''
    return "Python {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
def pythonIsCool():
    '''
    rtype: str
    '''
    return "Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''
    rtype: int
    '''
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
