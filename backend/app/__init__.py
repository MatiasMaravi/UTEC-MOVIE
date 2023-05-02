from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
import jwt
import datetime
from flask_cors import CORS
from models import setup_db, Genre, Movie, Director, User
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
        errors_to_send = []
        if db_user is not None:
            if db_user.username == username:
                errors_to_send.append('An account with this username already exists')

            if len(password) < 4:
                errors_to_send.append('The length of the password is too short')

            if len(errors_to_send) > 0:
                return jsonify({
                    'success': False,
                    'code': 422,
                    'messages': errors_to_send
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
    
    @app.route('/genres', methods=['GET'])
    def get_genres():
        genres= Genre.query.order_by('id').all()
        total_generes = Genre.query.count()
        if (total_generes == 0):
            abort(404)
        return jsonify({
            'success': True,
            'generes': [genere.format() for genere in genres],
            'total_generes': total_generes  
        })
    @app.route('/genres', methods=['POST'])
    def create_genres():
        body = request.get_json()
        name = body.get('name', None)
        search = body.get('search', None)
        if search:
            generes = Genre.order_by('id').filter(Genre.name.like('%{}%'.format(search))).all()
            return jsonify({
                'success': True,
                'generes': [genere.format() for genere in generes],
                'total_generes': len(generes)
            })
        else:
            if 'name' not in body:
                abort(422)
            response = {}
            try:
                genre = Genre(name=name)
                response['success'] = True
                genere_id = genre.insert()
                genre.id = genere_id
                response['genre'] = genre.format()

            except Exception as e:
                response['success'] = False
                print(e)
                abort(500)
            return jsonify(response)
    @app.route('/genres/<int_id>', methods=['DELETE'])
    def delete_genres(int_id):
        error_404 = False
        try:
            genre = Genre.query.get(int_id)
            if genre is None:
                error_404 = True
                raise Exception
            genre.delete()
            return jsonify({
                'success': True,
                'delete': int_id,
                'total_generes': Genre.query.count()
            })
        except Exception as e:
            if error_404:
                abort(404)
            else:
                abort(500)
    @app.route('/genres/<int_id>', methods=['PATCH'])
    def update_genres(int_id):
        response={}
        status_code=500
        try:
            genre=Genre.query.get(int_id)
            if genre is None:
                status_code=404
                raise Exception
            body = request.get_json()
            if 'name' in body:
                genre.name = body.get('name')
            response['success'] = True
            response['genre'] = genre.format()
            genre.update()
        except Exception as e:
            response['success'] = False
            print(e)
            abort(status_code)
        return jsonify(response)
    #MOVIES
    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies= Movie.query.order_by('id').all()
        total_movies = Movie.query.count()
        if (total_movies == 0):
            abort(404)
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies],
            'total_movies': total_movies  
        })
    @app.route('/movies', methods=['POST'])
    def create_movies():
        body = request.get_json()
        title = body.get('title', None)
        genre_id = body.get('genre_id', None)
        owner_id = body.get('owner_id', None)
        search = body.get('search', None)
        if search:
            movies = Movie.order_by('id').filter(Movie.title.like('%{}%'.format(search))).all()
            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies],
                'total_movies': len(movies)
            })
        else:
            if 'title' not in body:
                abort(422)
            if 'genre_id' not in body:
                abort(422)
            if 'owner_id' not in body:
                abort(422)

            response = {}
            try:
                movies = Movie(title=title, genre_id=genre_id, owner_id=owner_id)
                response['success'] = True
                movie_id = movies.insert()
                movies.id = movie_id
                response['movies'] = movies.format()

            except Exception as e:
                response['success'] = False
                print(e)
                abort(500)
            return jsonify(response)
    @app.route('/movies/<int_id>', methods=['DELETE'])
    def delete_movies(int_id):
        error_404 = False
        try:
            movies = Movie.query.get(int_id)
            if movies is None:
                error_404 = True
                raise Exception
            movies.delete()
            return jsonify({
                'success': True,
                'delete': int_id,
                'total_movies': Movie.query.count()
            })
        except Exception as e:
            if error_404:
                abort(404)
            else:
                abort(500)
    @app.route('/movies/<int_id>', methods=['PATCH'])
    def update_movies(int_id):
        response={}
        status_code=500
        try:
            movies=Movie.query.get(int_id)
            if movies is None:
                status_code=404
                raise Exception
            body = request.get_json()
            if 'title' in body:
                movies.title = body.get('title')
            if 'genre_id' in body:
                exist_genre = Genre.query.get(body.get('genre_id'))
                if exist_genre is None:
                    status_code=409
                    raise Exception
                movies.genre_id = body.get('genre_id')
            if 'owner_id' in body:
                exist_owner = User.query.get(body.get('owner_id'))
                if exist_owner is None:
                    status_code=409
                    raise Exception
                movies.owner_id = body.get('owner_id')
            response['success'] = True
            response['movies'] = movies.format()
            movies.update()
        except Exception as e:
            response['success'] = False
            print(e)
            abort(status_code)
        return jsonify(response)
    
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


