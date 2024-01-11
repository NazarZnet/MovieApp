from flask import Flask
from config import Config
from .api import MovieAPI

def create_app():
    app = Flask(__name__, static_url_path='/static')

    app.config.from_object(Config())

    app.movieapi = MovieAPI(app.config['MOVIEAPI_KEY'])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app