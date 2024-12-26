from flask import Flask
from flask_cors import CORS
from .routes import api_bp
import os

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for React frontend
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
    
    # App configuration
    app.config.from_pyfile('./config.py')
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
