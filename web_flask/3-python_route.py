#!/usr/bin/python3
"""Minimal Flask application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a simple greeting message.

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'.

    Returns:
        str: The string 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C' followed by the value of the 'text' variable.

    Args:
        text (str): The value captured from the URL dynamic segment.

    Returns:
        str: A string containing 'C' followed by the value of 'text'.
    """
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_print(text="is cool"):
    """ Display 'Python' followed by the value of the 'text' variable.

    Args:
        text (str): The value captured from the URL dynamic segment.

    Returns:
        str: A string containing 'Python' followed by the value of 'text'.
    """
    rst = text.replace('_', ' ')
    return "python {}".format(rst)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
