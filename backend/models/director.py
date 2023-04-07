from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
db = SQLAlchemy()

class Director(db.Model):
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
            
