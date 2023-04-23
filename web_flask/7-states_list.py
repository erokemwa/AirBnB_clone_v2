#!/usr/bin/python3

"""This module contains the app instance for the AirBnB Web"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Runs HTML page with sorted list of states"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception=None):
    """ends SQL Alchemy current Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
