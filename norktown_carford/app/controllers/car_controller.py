from ..models.car import Car
from ..models.owner import Owner
from .. import db
from flask import jsonify

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
        if owner.cars:
            return jsonify({'error': "Esse usuário ainda possui um carro associado a ele"}), 400
        db.session.delete(owner)
        db.session.commit()
        return jsonify({'message': 'Proprietário deletado com sucesso'}), 200
    return jsonify({'error': 'Proprietário não encontrado'}), 404
