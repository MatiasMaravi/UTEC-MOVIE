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

    @app.after_request
    def after_request(response):
        response.headers.add('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    @app.route('/genres', methods=['GET'])
    def get_genres():
        error_404= False
        try:
            genres= {genre.id: {'id': genre.id, 'name': genre.name} for genre in Genre.query.order_by('id').all()}
            if len(genres) == 0:
                error_404=True
                raise Exception
            return jsonify({
                'success': True,
                'genres': genres,
                'length': len(genres)
            }) 
        except Exception as e:
            if error_404:
                abort(404)
            else:
                abort(500)
    @app.route('/gnres', methods=['POST'])
    def create_genres():
        body = request.get_json()
        name = body.get('name', None)
        movies = body.get('movie', None)
        search = body.get('search', None)
        if search:
            generes = Genre.order_by('id').filter(Genre.name.like('%{}%'.format(search))).all()
            return jsonify({
                'success': True,
                'generes': [genere.format() for genere in generes],
                'total_generes': len(generes)
            })
        else:
            if 'name' or 'movie' not in body:
                abort(422)
            response = {}
            try:
                genere=Genre(name=name, movies=movies)
                response['success'] = True
                genere_id = genere.insert()
                genere.id = genere_id
                response['genere'] = genere.format()
            except Exception as e:
                response['success'] = False
                print(e)
                abort(500)
            return jsonify(response)
    @app.route('genres/<genere_id>', METHODS=['DELETE'])
    def delete_genere(genere_id):
        error_404 = False
        try:
            genere= Genre.query.get(genere_id)
            if generes is None:
                error_404 = True
                raise Exception
            genere.delete()
            return jsonify({
                'success': True,
                'deleted': genere_id,
                'total_genres': Genre.query.count()
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
    #MOVIES
    @app.route('/movies', methods=['GET'])
    def get_movies():
        error_404= False
        try:
            movies= {movie.id: {'id': movie.id,'title':movie.title,'genre_id':movie.genre_id,'owner_id':movie.owner_id} for movie in Movie.query.order_by('id').all()}
            if len(movies) == 0:
                error_404=True
                raise Exception
            return jsonify({
                'success': True,
                'movies': movies,
                'length': len(movies)
            }) 
        except Exception as e:
            if error_404:
                abort(404)
            else:
                abort(500)
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
            if 'title' or 'genre_id' or 'owner_id' not in body:
                abort(422)
            response = {}
            try:
                movie=Movie(title=title, genre_id=genre_id, owner_id=owner_id)
                response['success'] = True
                movie_id = movie.insert()
                movie.id = movie_id
                response['movie'] = movie.format()
            except Exception as e:
                response['success'] = False
                print(e)
                abort(500)
            return jsonify(response)
    @app.route('movies/<movie_id>', METHODS=['DELETE'])
    def delete_movie(movie_id):
        error_404 = False
        try:
            movie= Movie.query.get(movie_id)
            if movie is None:
                error_404 = True
                raise Exception
            movie.delete()
            return jsonify({
                'success': True,
                'deleted': movie_id,
                'total_movies': Movie.query.count()
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
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


