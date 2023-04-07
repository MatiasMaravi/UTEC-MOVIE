from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
from flask_cors import CORS
from models.__init__ import setup_db
from models.user import User
from models.movie import Movie
from models.genre import Genre
from models.director import Director
def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'utecuniversity'
    setup_db(app)
    CORS(app, origins=['http://localhost:8080', 'http://localhost:8080'])
    return app
