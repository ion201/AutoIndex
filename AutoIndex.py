#!/usr/bin/python3

import flask
import os

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def rootdir():
    return flask.render_template('Gallery.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)
