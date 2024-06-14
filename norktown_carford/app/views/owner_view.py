
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..controllers.owner_controller import create_owner, get_owner, update_owner, delete_owner
from ..dtos.owner_dto import OwnerDTO

owner_bp = Blueprint('owners', __name__)

@owner_bp.route('', methods=['POST'])
@jwt_required()
def add_owner():
    data = request.get_json()
    new_owner = create_owner(data)
    return jsonify(OwnerDTO(new_owner).serialize()), 201

@owner_bp.route('/<int:owner_id>', methods=['GET'])
@jwt_required()
def get_owner_route(owner_id):
    owner = get_owner(owner_id)
    if owner:
        return jsonify(OwnerDTO(owner).serialize())
    return jsonify({'error': 'Owner not found'}), 404

@owner_bp.route('/<int:owner_id>', methods=['PUT'])
@jwt_required()
def update_owner_route(owner_id):
    data = request.get_json()
    updated_owner = update_owner(owner_id, data)
    if updated_owner:
        return jsonify(OwnerDTO(updated_owner).serialize())
    return jsonify({'error': 'Owner not found'}), 404

@owner_bp.route('/<int:owner_id>', methods=['DELETE'])
@jwt_required()
def delete_owner_route(owner_id):
    response, status = delete_owner(owner_id)
    return response, status
