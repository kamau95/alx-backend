#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    defines babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


# initialize babel
babel = Babel(app)


@app.route("/", strict_slashes=False)
def page() -> str:
    """
    handle this / route
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
