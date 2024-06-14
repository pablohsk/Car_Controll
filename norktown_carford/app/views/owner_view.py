from flask import Blueprint, request, jsonify
from ..controllers.owner_controller import create_owner

owner_bp = Blueprint('owners', __name__)

@owner_bp.route('', methods=['POST'])
def add_owner():
    data = request.get_json()
    new_owner = create_owner(data)
    return jsonify({'id': new_owner.id}), 201
