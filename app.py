import logging
from datetime import timedelta
from flask import Flask, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv() # Cargar vairables de entorno

# Importar DB
from src.database.db import db

#Importar BLUEPRINTS
from src.routes.user_routes import user_bp
from src.routes.auth_routes import auth_bp
from src.routes.pet_routes import pet_bp
from src.routes.appointment_routes import appointment_bp
from src.routes.customer_routes import customer_bp

from config import app_config



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
    api_v1_bp.register_blueprint(pet_bp)
    api_v1_bp.register_blueprint(customer_bp)
    api_v1_bp.register_blueprint(appointment_bp)

    # Registrar Blueprint
    app.register_blueprint(api_v1_bp)

    return app

app = create_app()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app.run(debug=True, port=5001)