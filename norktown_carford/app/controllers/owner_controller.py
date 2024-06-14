from ..models.owner import Owner
from .. import db

def create_owner(data):
    new_owner = Owner(name=data['name'])
    db.session.add(new_owner)
    db.session.commit()
    return new_owner
