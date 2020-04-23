#!/usr/bin/python3
"""
A python script that uses flask
"""

from flask import Flask, render_template
from models import storage, State
from flask import escape

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def show_states():
    '''
    rtype: Dictionary: of States
    '''
    state_dict = storage.all(State)
    return render_template('7-states_list.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(self):
    '''
    Removes the current SQLAlchemy Session
    '''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
