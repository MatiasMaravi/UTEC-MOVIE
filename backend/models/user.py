from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
db = SQLAlchemy()

class User(db.Model):
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