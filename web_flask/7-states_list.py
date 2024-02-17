#!/usr/bin/python3
"""This is the 7-states_list module"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Displays a list of State objects sorted by name."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
