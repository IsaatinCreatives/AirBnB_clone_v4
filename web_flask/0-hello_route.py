#!/usr/bin/python3
"""
This is the first task in flask.
we are to display the index page.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The index page"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
