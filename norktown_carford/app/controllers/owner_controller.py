from flask import jsonify
from ..models.owner import Owner
from .. import db

def create_owner(data):
    new_owner = Owner(name=data['name'])
    db.session.add(new_owner)
    db.session.commit()
    return new_owner

def get_owner(owner_id):
    return Owner.query.get(owner_id)

def update_owner(owner_id, data):
    owner = Owner.query.get(owner_id)
    if owner:
        owner.name = data.get('name', owner.name)
        db.session.commit()
        return owner
    return None

def delete_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if owner:
        # Verificar se existem carros associados
        if owner.cars:
            return jsonify({'error': "Não foi possível deletar owner pois ainda há carros no seu nome"}), 400
        db.session.delete(owner)
        db.session.commit()
        return jsonify({'message': 'Owner deletado com sucesso'}), 200
    return jsonify({'error': 'Owner não encontrado'}), 404
