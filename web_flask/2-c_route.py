#!/usr/bin/python3
"""Starts a Flask web application.

This module starts a Flask web application that listens on
0.0.0.0, port 5000, and responds with various messages to
requests at different routes.
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """
    Displays 'Hello HBNB!' at the root URL.

    Returns:
        str: The message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Displays 'HBNB' at the /hbnb URL.

    Returns:
        str: The message 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_with_params(text):
    """
    Displays 'C' followed by the value of <text> at the /c/<text> URL.

    Args:
        text (str): The text to be displayed after 'C'.

    Returns:
        str: The message 'C' followed by the value of <text>, with
             underscores removed.
    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
