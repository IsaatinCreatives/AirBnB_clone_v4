#!/usr/bin/python3
"""displays filters"""

from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City
from models.state import State
import uuid


app = Flask(__name__)


@app.route('/0-hbnb', strict_slashes=False)
def hbnb_filters():
    """filters styate and city objects in database"""
    states = dict(sorted(storage.all("State").items()))
    amenity = dict(sorted(storage.all("Amenity").items()))
    places = dict(sorted(storage.all("Place").items()))
    return render_template('0-hbnb.html', title='AirBnB Clone',
                           states=states, amenities=amenity,
                           cache_id=uuid.uuid4(), places=places)


@app.teardown_appcontext
def destroy(exception):
    """Destroys the connection"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
