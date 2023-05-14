from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
from flask_cors import CORS
from .models import setup_db, Genre
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
            generes = Genre.order_by('id').filter(Genre.name.like(f'%{search}%')).all()
            return jsonify({
                'success': True,
                'generes': [genere.format() for genere in generes],
                'total_generes': len(generes)
            })
        else:
            if 'name' not in body:
                abort(422)
            
            response = {}
            
            # Verificar si el género ya existe en la base de datos
            existing_genre = Genre.query.filter_by(name=name).first()
            if existing_genre:
                response['success'] = False
                response['message'] = 'El género ya existe.'
                abort(409)
            else:
                try:
                    genre = Genre(name=name)
                    response['success'] = True
                    genre.id = genre.insert()
                    response['genre'] = genre.format()
                except Exception as e:
                    response['success'] = False
                    response['message'] = 'Error al crear el género.'
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

