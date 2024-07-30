#!/usr/bin/python3
"""
Starts a Flask web application.
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

    Replaces underscores in <text> with spaces.

    Args:
        text (str): The text to be displayed after 'C'.

    Returns:
        str: The message 'C' followed by the value of <text>, with
             underscores replaced by spaces.
    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_with_text_params(text):
    """
    Displays 'Python' followed by the value of <text> at the /python/<text> URL.

    Replaces underscores in <text> with spaces. If <text> is not provided,
    defaults to 'is cool'.

    Args:
        text (str): The text to be displayed after 'Python'.

    Returns:
        str: The message 'Python' followed by the value of <text>, with
             underscores replaced by spaces.
    """
    text_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_no_underscore)


@app.route('/number/<int:n>')
def number(n):
    """
    Displays 'n is a number' only if n is an integer.

    Args:
        n (int): The number to be displayed.

    Returns:
        str: The message '<n> is a number'.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
