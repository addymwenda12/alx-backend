#!/usr/bin/env python3
"""
This module defines a simple Flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Define the route for the home page("/")

    Returns:
    A rendered HTML template as a response
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
