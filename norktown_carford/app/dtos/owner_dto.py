from ..dtos.car_dto import CarDTO

class OwnerDTO:
    def __init__(self, owner):
        self.id = owner.id
        self.name = owner.name
        self.cars = [CarDTO(car).serialize() for car in owner.cars]

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'cars': self.cars
        }
