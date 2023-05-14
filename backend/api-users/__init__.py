from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
import jwt
import datetime
from flask_cors import CORS
from .models import setup_db, User, Is_Favorite

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'utecuniversity'
    setup_db(app)
    CORS(app, origins=['http://localhost:8080', 'http://localhost:8080'])

    @app.after_request
    def after_request(response):    
        response.headers.add('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')#Para https
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    @app.route('/register', methods=['POST'])
    def register():
        body = request.get_json()
        username = body.get('username', None)
        email = body.get('email', None)
        password = body.get('password', None)
        if email is None or username is None or password is None:
            abort(422)
        #Search
        db_user = User.query.filter(User.username==username).first()
        if db_user is not None:
            return jsonify({
                'success': False,
                'code': 422,
                'messages': 'An account with this username already exists'
            }), 422
        if len(str(password)) < 4:
            return jsonify({
                'success': False,
                'code': 422,
                'messages': 'The length of the password is too short'
            }), 422
        user = User(username=username, password=password,email=email)
        new_user_id = user.insert()

        token = jwt.encode({
            'id': new_user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return jsonify({
            'success': True,
            'token': str(token),
            'user_id': new_user_id
        })
    @app.route('/login', methods=['POST'])
    def login():
        body = request.get_json()
        username = body.get('username', None)
        password = body.get('password', None)
        if username is None or password is None:
            abort(422)
        user = User.query.filter(User.username==username).first()
        if user is None:
            return jsonify({
                'success': False,
                'code': 404,
                'messages': 'User not found'
            }), 404
        if user.password != password:
            return jsonify({
                'success': False,
                'code': 422,
                'messages': 'Incorrect password'
            }), 422
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return jsonify({
            'success': True,
            'token': str(token),
            'user_id': user.id
        })
    @app.route('/users', methods=['GET'])
    def get_users():
        users= User.query.order_by('id').all()
        total_users = User.query.count()
        if (total_users == 0):
            abort(404)
        return jsonify({
            'success': True,
            'users': [user.format() for user in users],
            'total_users': total_users  
        })
    @app.route('/users/<user_id>/favorites', methods=['GET'])
    def get_favorites(user_id):
        favorites = Is_Favorite.query.filter_by(user_id=user_id).all()
        if len(favorites) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'favorites': [favorite.format() for favorite in favorites],
            'total_favorites': len(favorites)
        })
    @app.route('/users/<user_id>/favorites', methods=['POST'])
    def create_favorite(user_id):
        body = request.get_json()
        movie_id = body.get('movie_id', None)
        if 'movie_id' not in body:
            abort(422)

        # Verificar si la película ya existe como favorita del usuario
        is_favorite = Is_Favorite.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        if is_favorite:
            return jsonify({
                'success': False,
                'error': 'La película ya está en la lista de favoritos del usuario'
            }), 422

        response = {}
        try:
            is_favorite = Is_Favorite(movie_id=movie_id, user_id=user_id)
            response['success'] = True
            is_favorite.id = is_favorite.insert()
            response['is_favorite'] = is_favorite.format()
        except Exception as e:
            response['success'] = False
            print(e)
            abort(500)
        return jsonify(response)


    @app.route('/users/<user_id>/favorites/<movie_id>', methods=['DELETE'])
    def delete_favorite(user_id, movie_id):
        status_code = 500
        try:
            is_favorite = Is_Favorite.query.filter_by(user_id=user_id, movie_id=movie_id).one_or_none()
            if is_favorite is None:
                status_code = 404
                raise Exception
            is_favorite.delete()
            return jsonify({
                'success': True,
                'delete': movie_id,
            })
        except Exception as e:
            print(e)
            abort(status_code)



    #----handling errorrs-----
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            "message": "resource not found"
        }), 404
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            "message": "unprocessable entity"
        }), 422
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            "message": "internal server error"
        }), 500
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            "message": "bad request"
        }), 400
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405
    @app.errorhandler(409)
    def conflict(error):
        return jsonify({
            'success': False,
            'error': 409,
            'message': 'resource already exists'
        }), 409
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized'
        }), 401
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'forbidden'
        }), 403
    return app