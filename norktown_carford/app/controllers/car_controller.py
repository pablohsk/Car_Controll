from ..models.car import Car
from ..models.owner import Owner
from .. import db

def create_car(data):
    owner = Owner.query.get(data['owner_id'])
    if owner and len(owner.cars) < 3:
        new_car = Car(color=data['color'], model=data['model'], owner_id=data['owner_id'])
        db.session.add(new_car)
        db.session.commit()
        return new_car
    return None
