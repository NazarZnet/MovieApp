from flask import Flask
from config import Config
from .api import MovieAPI

def create_app():
    from .extensions import jwt, db

    app = Flask(__name__, static_url_path='/static')

    app.config.from_object(Config())

    app.movieapi = MovieAPI(app.config['MOVIEAPI_KEY'])

    jwt.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    with app.app_context():
        db.create_all()
    return app