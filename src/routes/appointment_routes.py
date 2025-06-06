from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.database.db import db
from src.models.appointment_model import Appointment
from src.models.user_model import User
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import logging

# Define el Blueprint para las rutas de users
appointment_bp = Blueprint('appointment_bp', __name__, url_prefix='/appointments')


@appointment_bp.route('/', methods=['GET'])
@jwt_required()
def get_appointments():
    appointments = Appointment.query.all()
    appointment_list = [appointment.to_dict() for appointment in appointments]

    if appointments:
        return jsonify(appointment_list), 200
    else:
        return jsonify({'message': 'No appointments'}), 404


@appointment_bp.route('/<string:dni>', methods=['GET'])
@jwt_required()
def get_appointment_by_userid(dni):
    # Hago al consulta pra sacar el usuario deseado.
    appointments = Appointment.query.filter_by(user_id=dni)
    appointment_list = [appointment.to_dict() for appointment in appointments]

    if appointments:
        return jsonify(appointment_list), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@appointment_bp.route('/', methods=['POST'])
@jwt_required()
def create_appointment():

    # Obtener ID(dni) usuario actual.
    current_user_dni = get_jwt_identity()
    # Sacamos su rol desde la BD
    current_user = User.query.filter_by(dni=current_user_dni).first()

    # Verifica si el usuario actual tiene el rol de administrador
#    if current_user.rol != 'gest' or current_user.rol != 'vet':
#        logging.info(f"ROL USUARIO: {current_user.rol}")
#        return jsonify({'message': 'Unauthorized: Only users with the rol gest or vet are able to create customers'}), 403

    data = request.get_json()

    # id = data['id']
    type = data['type']
    description = data['description']
    date = data['date']
    user_id = data['user_id'] # Al veterinario que llevará a cabo el tratamiento
    pet_id = data['pet_id']

    if not id or not type or not description or not date or not user_id or not pet_id:
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        new_appointment = Appointment( type=type, description=description, date=date, user_id=user_id, pet_id=pet_id)
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        logging.exception('IntegrityError')
        return jsonify({'message': 'Error creating apointment'}), 409
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating Appointment: {e}")
        return jsonify({'message': 'Error creating Appointment'}), 500

@appointment_bp.route('/<string:id>', methods=['DELETE'])
@jwt_required()
def delete_appointment(id):
    appointment = Appointment.query.filter_by(id=id).first()

    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'}), 200
    else:
        return jsonify({'message': 'Appointment not found'}), 404


