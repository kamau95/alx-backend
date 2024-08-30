#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, Babel, render_template


app = Flask(__name__)


# configure supported languages
app.config['LANGUAGES'] = ['en', 'fr']


# configure default langua
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


# configure default timezone
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


# initialize babel
babel = Babel(app)


@app.route("/")
def page() -> str:
    """
    handle this / route
    """
    return render_template("1-index.html")


if '__main__' == '__name__':
    app.run(debug=True)
