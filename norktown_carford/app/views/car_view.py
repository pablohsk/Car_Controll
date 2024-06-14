from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..controllers.car_controller import create_car, get_car, update_car, delete_car
from ..dtos.car_dto import CarDTO

car_bp = Blueprint('cars', __name__)

@car_bp.route('', methods=['POST'])
@jwt_required()
def add_car():
    data = request.get_json()
    new_car = create_car(data)
    if new_car:
        return jsonify(CarDTO(new_car).serialize()), 201
    return jsonify({'error': 'Owner not found or car limit reached'}), 400

@car_bp.route('/<int:car_id>', methods=['GET'])
@jwt_required()
def get_car_route(car_id):
    car = get_car(car_id)
    if car:
        return jsonify(CarDTO(car).serialize())
    return jsonify({'error': 'Car not found'}), 404

@car_bp.route('/<int:car_id>', methods=['PUT'])
@jwt_required()
def update_car_route(car_id):
    data = request.get_json()
    updated_car = update_car(car_id, data)
    if updated_car:
        return jsonify(CarDTO(updated_car).serialize())
    return jsonify({'error': 'Car not found'}), 404

@car_bp.route('/<int:car_id>', methods=['DELETE'])
@jwt_required()
def delete_car_route(car_id):
    if delete_car(car_id):
        return jsonify({'message': 'Car deleted'}), 200
    return jsonify({'error': 'Car not found'}), 404
