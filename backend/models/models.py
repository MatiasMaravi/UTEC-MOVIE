from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
database_name="cloud_proyect"
database_path="postgres://{}@{}/{}".format('jerimy:12345','localhost:5432', database_name)
# por el momento el database name lo trabajaremos en postgres.

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    with app.app_context():
        db.init_app(app)
        db.create_all()



class User(db.model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    movies = relationship("Movie", back_populates="owner")

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
#fijarse en la clase movie, cambie gnere por gneres, ya que es una relacion de muchos a muchos.
#Matias coloco gnere, pero no se si sea correcto.
class Movie(db.model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="movies")
    genres = relationship("Genres", back_populates="movies")
    def __repr__(self):
        return f"Movie: id: {self.id}, title: {self.title}, genre_id: {self.genre_id} , owner_id: {self.owner_id}, owner: {self.owner} ,genres: {self.genres}"
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

#Cambiar owner por director
class Genre(db.model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    movies = relationship("Movie", back_populates="genre")
    def __repr__(self):
        return f"Genre: id: {self.id}, name: {self.name}, movies: {self.movies}"
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_genre = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_genre
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

class Actor(db.model):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sex = Column(String, index=True)
    credits = relationship("Credits", back_populates="actor")
    def __repr__(self):
        return f"Actor: id:{self.id}, name:{self.name}, sex:{self.sex}"
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

class Credits(db.model):
    __tablename__ = "credits"
    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey("actors.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))

    actor = relationship("Actor", back_populates="credits")
    movie = relationship("Movie", back_populates="credits")
    def __repr__(self):
        return f"Credits: id:{self.id}, actor_id:{self.actor_id}, movie_id:{self.movie_id}, actor:{self.actor}, movie:{self.movie}"
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            create_credits = self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return create_credits
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

class Director(db.model):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    biography = Column(String, index=True)
    birth_date = Column(String, index=True)
    def __repr__(self):
        return f"Director: id:{self.id}, name:{self.name}, biography:{self.biography}, birth_date:{self.birth_date}"
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
            
