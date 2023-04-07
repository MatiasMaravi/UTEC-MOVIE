from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
db = SQLAlchemy()


class Genre(db.Model):
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

class Actor(db.Model):
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