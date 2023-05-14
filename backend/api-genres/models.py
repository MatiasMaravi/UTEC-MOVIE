from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Config:
    # Obtener la clave secreta de la variable de entorno SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Obtener la URI de la base de datos de la variable de entorno DATABASE_URI
    DATABASE_URI = os.getenv('DATABASE_URI')

db = SQLAlchemy()
database_path="postgresql://postgres:N94P1SJh3ZUfzE3ApZCy@cloud.cxbbb0awctld.us-east-1.rds.amazonaws.com:5432/cloud"

#Ejemplo: DATABASE_URI=postgresql://postgres:123@localhost:5432/utecmovie2023
# por el momento el database name lo trabajaremos en postgres.
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    with app.app_context():
        db.init_app(app)
        db.create_all()

class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True)
    movies = db.relationship("Movie", back_populates="genres")
    def __repr__(self):
        return f"Genre: id: {self.id}, name: {self.name}, movies: {self.movies}"
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_id = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
        return create_id
    
    def update(self):
        error= False
        try:
            print('self: ',self)
            db.session.commit()
        except Exception as e:
            print('error: ',e)
            error= True
            db.session.rollback()
        finally:
            db.session.close()
        return error
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String, index=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))

    genres = db.relationship("Genre", back_populates="movies")
    is_favorite = db.relationship("Is_Favorite", back_populates="movie")
    def __repr__(self):
        return f"Movie: id: {self.id}, title: {self.title}, genre_id: {self.genre_id},genres: {self.genres}"
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre_id': self.genre_id,
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_movie = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_movie
    def update(self):
        error= False
        try:
            print('self: ',self)
            db.session.commit()
        except Exception as e:
            print('error: ',e)
            error= True
            db.session.rollback()
        finally:
            db.session.close()
        return error
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    is_favorite = db.relationship("Is_Favorite", back_populates="user")

    def __repr__(self):
        return f"User: id: {self.id}, username: {self.username}, email: {self.email} , password: {self.password}"
    def format(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_user = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_user
    
    def update(self):
        error= False
        try:
            print('self: ',self)
            db.session.commit()
        except Exception as e:
            print('error: ',e)
            error= True
            db.session.rollback()
        finally:
            db.session.close()
        return error
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

class Is_Favorite(db.Model):
    __tablename__ = "is_favorite"
    id = db.Column(db.Integer, primary_key=True, index=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    movie = db.relationship("Movie", back_populates="is_favorite")
    user = db.relationship("User", back_populates="is_favorite")
    def __repr__(self):
        return f"Is_Favorite: id: {self.id}, movie_id: {self.movie_id}, user_id: {self.user_id} , movie: {self.movie} , user: {self.user}"
    def format(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "user_id": self.user_id,
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_is_favorite = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_is_favorite
    
    def update(self):
        error= False
        try:
            print('self: ',self)
            db.session.commit()
        except Exception as e:
            print('error: ',e)
            error= True
            db.session.rollback()
        finally:
            db.session.close()
        return error
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()