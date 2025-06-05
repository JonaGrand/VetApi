import logging
from datetime import timedelta

from flask import Flask, Blueprint
from dotenv import load_dotenv
import os

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from src.routes.auth_routes import auth_bp

load_dotenv() # Cargar vairables de entorno

# Importar DB
from src.database.db import db

#Importar BLUEPRINTS
from src.routes.user_routes import user_bp

from config import app_config

from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Configurar CORS para permitir solicitudes desde localhost
    CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

    # Cargar configuración desde config.py
    app.config.from_object(app_config)

    # Inicializar jwt
    jwt = JWTManager(app)

    # Inicializar SQLAlchemy
    db.init_app(app)

    # -- BLUEPRINTS --
    # - Base
    api_v1_bp = Blueprint('api_v1_bp', __name__, url_prefix='/api/v1')
    # Resto
    api_v1_bp.register_blueprint(auth_bp)
    api_v1_bp.register_blueprint(user_bp)

    # Registrar Blueprint
    app.register_blueprint(api_v1_bp)

    return app

app = create_app()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app.run(debug=True, port=5001)