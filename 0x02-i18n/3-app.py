#!/usr/bin/env python3
"""
This module defines a simple Flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    Define the route for the home page("/")

    Returns:
    A rendered HTML template as a response
    """
    return render_template('3-index.html', title=_("home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
