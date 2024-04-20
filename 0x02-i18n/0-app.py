#!/usr/bin/env python3
"""
This module defines a simple Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """
    Define the route for the home page("/")

    Returns:
    A rendered HTML template as a response
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
