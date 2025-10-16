#!/usr/bin/python

import os
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def index():
    response = make_response("changed")

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
