#!/usr/bin/python3
""" a script that starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__, template_folder='./templates')
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def states_list(id='0'):
    ''' returns a HTML page '''
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(), id=id)


@app.teardown_appcontext
def close_session(response_or_exc):
    ''' closes session SQLAlchemy '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
