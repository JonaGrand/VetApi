# config.py
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() == 'true'

    # Configuración JWT
    JWT_SECRET_KEY = os.getenv('JWT_KEY')
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)
    JWT_SESSION_COOKIE = False  # Para aplicar la caducidad
    JWT_COOKIE_CSRF_PROTECT = False  # Considera habilitarlo en producción
    JWT_COOKIE_SECURE = False  # True en producción con HTTPS
    JWT_COOKIE_SAMESITE = "Lax"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    JWT_COOKIE_SECURE = True # Forzar HTTPS para cookies en producción

# Puedes añadir más configuraciones (TestingConfig, etc.)

# Selecciona la configuración a usar, por ejemplo, basándote en una variable de entorno
# Por defecto, usa DevelopmentConfig si FLASK_ENV no está configurado o es 'development'
config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig
)

key = os.getenv('FLASK_ENV', 'development')
app_config = config_by_name[key]