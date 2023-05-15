from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
from flask_cors import CORS
from .models import setup_db, Genre, Movie
def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'utecuniversity'
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):    
        response.headers.add('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')#Para https
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
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
    @app.route('/movies/<int_id>', methods=['GET'])
    def get_movies_by_id(int_id):
        movie = Movie.query.get(int_id)
        if movie is None:
            abort(404)
        return jsonify({
            'success': True,
            'movies': movie.format()
        })

    @app.route('/movies', methods=['POST'])
    def create_movies():
        body = request.get_json()
        title = body.get('title', None)
        genre_id = body.get('genre_id', None)
        search = body.get('search', None)
        
        if search:
            movies = Movie.order_by('id').filter(Movie.title.like(f'%{search}%')).all()
            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies],
                'total_movies': len(movies)
            })
        
        elif title and genre_id:
            # Comprobamos si la película ya existe
            existing_movie = Movie.query.filter_by(title=title, genre_id=genre_id).first()
            if existing_movie:
                abort(409, 'La película ya existe.')
            
            # Si la película no existe, la agregamos
            try:
                movie = Movie(title=title, genre_id=genre_id)
                movie.insert()
                response = {
                    'success': True,
                    'movies': movie.format()
                }
            except:
                abort(500)
        else:
            abort(422)
            
        return jsonify(response)

    @app.route('/movies/<int_id>', methods=['DELETE'])
    def delete_movies(int_id):
        status_code = 500
        try:
            movies = Movie.query.get(int_id)
            if movies is None:
                status_code = 404
                raise Exception
            movies.delete()
            return jsonify({
                'success': True,
                'delete': int_id,
                'total_movies': Movie.query.count()
            })
        except Exception as e:
            print(e)
            abort(status_code)
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


