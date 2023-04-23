#!/usr/bin/python3
"""
a script starts Flask web app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """returns C followed by a formated text value"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_is_cool(text="is cool"):
    """returns Python, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """returns 'n' is a number” only if n is an integer """
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """returns a HTML page only if n is an intege”"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """returns a HTML page only if n is an integer"""
    if n % 2 == 0:
        is_odd_or_even = "even"
    else:
        is_odd_or_even = "odd"

    return render_template("6-number_odd_or_even.html", p=n, m=is_odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
