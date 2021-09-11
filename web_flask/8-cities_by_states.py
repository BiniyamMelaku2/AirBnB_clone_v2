#!/usr/bin/python3
""" a script that starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City


app = Flask(__name__, template_folder='./templates')
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    ''' returns a HTML page '''
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def close_session(response_or_exc):
    ''' closes session SQLAlchemy '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
