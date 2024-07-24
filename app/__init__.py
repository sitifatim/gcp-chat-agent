from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__,template_folder='../templates', static_folder='../static', static_url_path='/')
    if os.environ.get('FLASK_ENV') == 'development':
        CORS(app)
    from app.routes.routes import app_routes
    app.register_blueprint(app_routes)
    return app