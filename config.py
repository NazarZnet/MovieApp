from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        # Get Flask configurations from environment variables
        self.DEBUG = os.getenv('FLASK_DEBUG', False)
        self.HOST = os.getenv('FLASK_HOST', 'localhost')
        self.PORT = os.getenv('FLASK_RUN_PORT', 5000)
        self.SECRET_KEY = os.getenv('SECRET_KEY', '11111')
        self.MOVIEAPI_KEY = os.getenv('MOVIEAPI_KEY')

        #authorizatio configurations
        self.JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')

        #database configurations
        self.SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
