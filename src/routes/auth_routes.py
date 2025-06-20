from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, get_jti, decode_token, \
    jwt_required, get_jwt
from src.database.db import db
from src.models.user_model import User
from src.models.session_model import Session


from sqlalchemy.exc import IntegrityError
from datetime import datetime
import logging

# Define el Blueprint para las rutas de empleados
auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    dni_input = request.json.get("dni", None) # Renombrado para claridad
    password = request.json.get("password", None)

    # Consulta a la BD
    user = User.query.filter_by(dni=dni_input).first()

    if not user or not user.check_password(password):  # Usa el metodo check_password.
        return jsonify({"msg": "DNI o contraseña incorrectos"}), 401

    try:
        # Eliminar sesiones existentes para este usuario ANTES de crear una nueva.
        # Se usa user.dni para asegurar que es el DNI canónico de la base de datos.
        Session.query.filter_by(user_id=user.dni).delete()

        # Se crea el JWT
        access_token = create_access_token(identity=user.dni)
        jti = get_jti(access_token)

        # Se decodifica el token para poder ver el expiration date
        decoded_token = decode_token(access_token)
        expiration_time = datetime.fromtimestamp(decoded_token['exp'])
        # logging.error(expiration_time) # Comentado como en tu código original

        # Se crea el nuevo registro en la base de datos
        new_session = Session(
            id=jti,
            user_id=user.dni,
            expires_at=expiration_time
        )
        db.session.add(new_session)
        db.session.commit() # Hace la modificación

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error al procesar el login y la sesión: {e}") # Log más descriptivo
        return jsonify({"msg": "Error interno al procesar el login"}), 500

    # Si todo va bien, devuelve la respuesta
    response = jsonify({"msg": "login successful", "rol": user.rol})
    set_access_cookies(response, access_token)
    return response, 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Cojo el jti (id del jwt) que devuelve el front
    jti = get_jwt()['jti']

    session = Session.query.get(jti)
    if session:
        db.session.delete(session)
        db.session.commit()
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response) # Indico al navegador que no use el token. Forma cutre de invalidar sesión
    return response, 200