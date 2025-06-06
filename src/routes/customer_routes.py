# Define el Blueprint para las rutas de users
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.database.db import db
from src.models.customer_model import Customer
from src.models.user_model import User
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import logging

customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')

@customer_bp.route('/', methods=['GET'])
@jwt_required()
def get_customers():
    customers = Customer.query.all()
    customer_list = [customer.to_dict() for customer in customers]

    if customers:
        return jsonify(customer_list), 200
    else:
        return jsonify({'message': 'No customers found'}), 404

@customer_bp.route('/<string:dni>', methods=['GET'])
@jwt_required()
def get_customer_by_dni(dni):
    # Hago al consulta pra sacar el usuario deseado.
    customer = Customer.query.filter_by(dni=dni).first()

    if customer:
        return jsonify(customer.to_dict()), 200
    else:
        return jsonify({'message': 'Customer not found'}), 404

# Solo deberia de poder crear Customers (clientes) el rol vet y gest
@customer_bp.route('/', methods=['POST'])
@jwt_required()
def create_customer():

    # Obtener ID(dni) usuario actual.
    current_user_dni = get_jwt_identity()
    # Sacamos su rol desde la BD
    current_user = User.query.filter_by(dni=current_user_dni).first()

    # Verifica si el usuario actual tiene el rol de administrador
#    if current_user.rol != 'gest' or current_user.rol != 'vet':
#        return jsonify({'message': 'Unauthorized: Only users with the rol gest or vet are able to create customers'}), 403

    data = request.get_json()

    dni = data.get('dni')
    name = data.get('name')
    surnames = data.get('surnames')
    mail = data.get('mail')
    phone = data.get('phone')

    if not dni or not name or not surnames or not mail or not phone:
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        new_customer = Customer(dni=dni, name=name, surnames=surnames, mail=mail, phone=phone)
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Customer already exists'}), 409
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating Customer: {e}")
        return jsonify({'message': 'Error creating customer'}), 500

@customer_bp.route('/<string:dni>', methods=['DELETE'])
@jwt_required()
def delete_customer(dni):
    customer = Customer.query.filter_by(dni=dni).first()

    if customer:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted successfully'}), 200
    else:
        return jsonify({'message': 'Customer not found'}), 404