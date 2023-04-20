#!/usr/bin/python3
""" script displays Python is cool! """

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """displays Hello HBNB!"""
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """displays C followed by a formated text value"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyiscool(text="is cool"):
    """ display Python, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
