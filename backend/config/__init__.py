import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of the SECRET_KEY environment variable
SECRET_KEY = os.getenv('SECRET_KEY')

# Define the configuration for the app
class Config:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
