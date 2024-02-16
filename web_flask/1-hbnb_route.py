#!/usr/bin/python3
"""this is flask app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return f"Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def rout_hbnb():
    return f"HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
