#!/usr/bin/python3
"""sorts cities and states from the database
"""

from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City
from models.state import State


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """filters the states and cities from database"""
    states = dict(sorted(storage.all("State").items()))
    amenity = dict(sorted(storage.all("Amenity").items()))
    return render_template('10-hbnb_filters.html', title='AirBnB Clone',
                           states=states, amenities=amenity)


@app.teardown_appcontext
def destroy(exception):
    """Destroys the connection"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
