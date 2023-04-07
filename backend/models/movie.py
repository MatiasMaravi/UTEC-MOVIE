from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="movies")
    genres = relationship("Genre", back_populates="movies")
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
