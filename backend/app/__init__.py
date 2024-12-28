from flask import Flask, send_from_directory
from flask_cors import CORS
from .routes import api_bp
import os

def create_app():
    app = Flask(__name__,static_folder='../../frontend/build',static_url_path='/')
    
    # Enable CORS for React frontend
    CORS(app, resources={r"/*": {"origins": ['*']}})
    
    @app.route("/")
    def serve():
        return send_from_directory(app.static_folder, "index.html")

    # Fallback for React routes (SPA)
    @app.errorhandler(404)
    def not_found(e):
        return send_from_directory(app.static_folder, "index.html")
    
    # App configuration
    app.config.from_pyfile('./config.py')
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
