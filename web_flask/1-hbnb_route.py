#!/usr/bin/python3
"""Starts a Flask web application with two routes:
    - /: Displays 'Hello HBNB!'
    - /hbnb: Displays 'HBNB'
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """
    Displays 'Hello HBNB!'

    Returns:
        str: The message 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Displays 'HBNB'

    Returns:
        str: The message 'HBNB'
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
