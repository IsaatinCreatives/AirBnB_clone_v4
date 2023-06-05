#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python: default
    /python/: default
    /python/<text>: displays the text on a page 
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """The first route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """Checks if text is string"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    """Provides 3 options for routing"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
