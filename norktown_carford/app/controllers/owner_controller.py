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
        db.session.delete(owner)
        db.session.commit()
        return True
    return False
