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

def get_car(car_id):
    return Car.query.get(car_id)

def update_car(car_id, data):
    car = Car.query.get(car_id)
    if car:
        car.color = data.get('color', car.color)
        car.model = data.get('model', car.model)
        db.session.commit()
        return car
    return None

def delete_car(car_id):
    car = Car.query.get(car_id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return True
    return False
