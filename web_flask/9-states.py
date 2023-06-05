#!/usr/bin/python3
"""accepts a GET request and checks whether parameter passed matches state id,
if match, it displays the state associated with the id else displays an error
page
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """lists all the State objects"""
    all_states = storage.all('State')
    sorted_dic = dict(sorted(all_states.items()))
    return render_template('9-states.html', storage=sorted_dic,
                           states="State", title="HBNB")


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays the state based on the id"""
    all_states = dict(sorted(storage.all('State').items()))
    for state_id, state in all_states.items():
        if state.id == id:
            return render_template('9-states.html', storage=all_states,
                                   states="State", city="City", title="HBNB")
    return "<h1>Not found!</h1>"


@app.teardown_appcontext
def destroy(exception):
    """Destroys the sqlaclhemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
