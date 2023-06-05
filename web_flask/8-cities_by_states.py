#!/usr/bin/python3
"""
displays cities based on states,
and displays it on the page.
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """lists all the State objects"""
    all_states = storage.all('State')
    sorted_dic = dict(sorted(all_states.items()))
    return render_template('8-cities_by_states.html', storage=sorted_dic,
                           states="State", title="HBNB")


@app.teardown_appcontext
def destroy(exception):
    """Destroys the sqlaclhemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
