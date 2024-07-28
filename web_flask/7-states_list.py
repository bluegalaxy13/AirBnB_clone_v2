#!/usr/bin/python
"""_summary_
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """

    Args:
        exception (_type_): _description_
    """
    storage.close()
    
@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)
    