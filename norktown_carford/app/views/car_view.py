from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from ..controllers.car_controller import create_car

car_bp = Blueprint('cars', __name__)

@car_bp.route('', methods=['POST'])
@jwt_required()
def add_car():
    data = request.get_json()
    new_car = create_car(data)
    if new_car:
        return jsonify({'id': new_car.id}), 201
    return jsonify({'error': 'Owner not found or car limit reached'}), 400

@car_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    access_token = create_access_token(identity=data['username'])
    return jsonify(access_token=access_token), 200
