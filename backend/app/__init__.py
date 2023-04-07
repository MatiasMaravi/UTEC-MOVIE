from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
from flask_cors import CORS
from models import setup_db
def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'utecuniversity'
    setup_db(app)
    CORS(app, origins=['http://localhost:8080', 'http://localhost:8080'])
    return app