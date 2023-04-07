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