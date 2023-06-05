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
    /number/<int:n>: displays n on the page if a number
    /number_template/<int:n>: displays even|odd
    /number_odd_or_even/<int:n>: dispplays even|odd
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This is the index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """First route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """Displays a GET request"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """checks if a number and displays it"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numtemplate(n):
    """checks if n is a number"""
    return render_template('5-number_template.html', number=n, title="HBNB")


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """checks if n is odd or even"""
    return render_template('6-number_odd_or_even.html', number=n, title="HBNB")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
