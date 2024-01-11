from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        # Get Flask configurations from environment variables
        self.DEBUG = os.getenv('FLASK_DEBUG', False)
        self.HOST = os.getenv('FLASK_HOST', 'localhost')
        self.PORT = os.getenv('FLASK_RUN_PORT', 5000)
        self.SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
        self.MOVIEAPI_KEY = os.getenv('MOVIEAPI_KEY', 'your-movieapi-key')
        # Add more configurations as needed
