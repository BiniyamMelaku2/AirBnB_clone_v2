#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    ''' returns a simple page '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    ''' returns a string '''
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    ''' returns c page '''
    text = text.replace('_', ' ')
    return 'C ' + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
