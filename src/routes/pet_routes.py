from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.database.db import db
from src.models.pet_model import Pet
from src.models.user_model import User
from sqlalchemy.exc import IntegrityError

import logging

# Define el Blueprint para las rutas de Pets
pet_bp = Blueprint('pet_bp', __name__, url_prefix='/pets')

@pet_bp.route('/', methods=['GET'])
@jwt_required()
def get_pets():
    pets = Pet.query.all()
    pets_list = [pet.to_dict() for pet in pets]

    if pets:
        return jsonify(pets_list), 200
    else:
        return jsonify({'message': 'No pets found'}), 404


@pet_bp.route('/<string:num_chip>', methods=['GET'])
@jwt_required()
def get_pet_by_chip(num_chip):
    # Hago al consulta pra sacar el pet deseado.
    pet = Pet.query.filter_by(num_chip=num_chip).first()

    if pet:
        return jsonify(pet.to_dict()), 200
    else:
        return jsonify({'message': 'Pet not found'}), 404
    
# Solo deberia poder crear mascotas el usuario gest o vet
@pet_bp.route('/', methods=['POST'])
@jwt_required()
def create_pet():
    data = request.get_json()

    num_chip = data.get('num_chip')
    name = data.get('name')
    birth_date = data.get('birth_date')
    animal = data.get('animal')
    breed = data.get('breed')
    customer_id = data.get('customer_id')


    if not num_chip or not name or not birth_date or not animal or not breed or not customer_id:
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        new_pet = Pet(num_chip=num_chip, name=name, birth_date=birth_date, animal=animal, breed=breed, customer_id=customer_id)
        db.session.add(new_pet)
        db.session.commit()
        return jsonify({'message': 'Pet created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Pet already exists'}), 409
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating pet: {e}")
        return jsonify({'message': 'Error creating pet'}), 500

@pet_bp.route('/<string:num_chip>', methods=['DELETE'])
@jwt_required()
def delete_pet(num_chip):
    pet = Pet.query.filter_by(num_chip=num_chip).first()

    if pet:
        db.session.delete(pet)
        db.session.commit()
        return jsonify({'message': 'Pet deleted successfully'}), 200
    else:
        return jsonify({'message': 'Pet not found'}), 404
