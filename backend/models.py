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
database_path=Config.DATABASE_URI
#Ejemplo: DATABASE_URI=postgresql://postgres:123@localhost:5432/utecmovie2023
# por el momento el database name lo trabajaremos en postgres.
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    with app.app_context():
        db.init_app(app)
        db.create_all()

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True)
    biography = db.Column(db.String, index=True)
    birth_date = db.Column(db.String, index=True)
    def __repr__(self):
        return f"Director: id:{self.id}, name:{self.name}, biography:{self.biography}, birth_date:{self.birth_date}"
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'biography': self.biography,
            'birth_date': self.birth_date
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_director = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_director
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

class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True)
    genero = db.Column(db.String, index=True)
    def __repr__(self):
        return f"Actor: id:{self.id}, name:{self.name}, genero:{self.genero}"
    def format(self):{
            'id': self.id,
            'name': self.name,
            'genero': self.genero
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_actor = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_actor
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
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    owner = db.relationship("User", back_populates="movies")
    genres = db.relationship("Genre", back_populates="movies")
    def __repr__(self):
        return f"Movie: id: {self.id}, title: {self.title}, genre_id: {self.genre_id} , owner_id: {self.owner_id}, owner: {self.owner} ,genres: {self.genres}"
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre_id': self.genre_id,
            'owner_id': self.owner_id
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
    movies = db.relationship("Movie", back_populates="owner")

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