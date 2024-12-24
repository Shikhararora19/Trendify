from flask import Flask
from app.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(routes)
    return app
