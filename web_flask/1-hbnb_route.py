#!/usr/bin/python3
"""
Displays 'HBNB'
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """first route"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
