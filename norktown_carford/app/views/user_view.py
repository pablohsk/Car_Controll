from flask import Blueprint, request, jsonify
from ..controllers.user_controller import create_user, authenticate_user
from flask_jwt_extended import create_access_token

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = create_user(data)
    if new_user:
        return jsonify({'message': 'User created successfully'}), 201
    return jsonify({'error': 'User already exists'}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate_user(data['username'], data['password'])
    if user:
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
