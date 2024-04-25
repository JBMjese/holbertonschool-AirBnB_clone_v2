#!/usr/bin/python3
"""Minimal Flask application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display a simple greeting message.

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'.

    Returns:
        str: The string 'HBNB'.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
