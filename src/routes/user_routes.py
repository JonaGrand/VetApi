from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.database.db import db
from src.models.user_model import User
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import logging

# Define el Blueprint para las rutas de users
user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    rol = request.args.get('rol')
    query = User.query

    # Si se le infica un rol por los parametros, se filtra
    if rol:
        query = query.filter_by(rol=rol)

    # Se hace la función
    users = query.all()
    user_list = [user.to_dict() for user in users]
    if users:
        return jsonify(user_list), 200
    else:
        return jsonify({'message': 'No users'}), 404


@user_bp.route('/<string:dni>', methods=['GET'])
@jwt_required()
def get_user_by_dni(dni):
    # Hago al consulta pra sacar el usuario deseado.
    user = User.query.filter_by(dni=dni).first()

    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# Solo deberia de poder crear usuarios (empleados) el rol "admin"
@user_bp.route('/', methods=['POST', 'OPTIONS'])
@jwt_required()
def create_user():

    # Obtener ID(dni) usuario actual.
    current_user_dni = get_jwt_identity()
    # Sacamos su rol desde la BD
    current_user = User.query.filter_by(dni=current_user_dni).first()

    # Verifica si el usuario actual tiene el rol de administrador
    if current_user.rol != 'admin':
        return jsonify({'message': 'Unauthorized: Only admins can create users'}), 403

    data = request.get_json()

    dni = data.get('dni')
    name = data.get('name')
    password = data.get('password')
    surnames = data.get('surnames')
    rol = data.get('rol')
    mail = data.get('mail')
    phone = data.get('phone')
    admission_date = data.get('admission_date')

    if not dni or not password or not rol or not name or not surnames or not mail or not phone or not admission_date:
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        new_user = User(dni=dni, password=password, rol=rol, name=name, surnames=surnames, mail=mail, phone=phone, admission_date=admission_date)
        new_user.set_password(password) # Hashear contraseña
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User already exists'}), 409
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating user: {e}")
        return jsonify({'message': 'Error creating user'}), 500

@user_bp.route('/<string:dni>', methods=['DELETE'])
@jwt_required()
def delete_user(dni):
    user = User.query.filter_by(dni=dni).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


