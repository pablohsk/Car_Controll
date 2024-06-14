class CarDTO:
    def __init__(self, car):
        self.id = car.id
        self.color = car.color
        self.model = car.model
        self.owner_id = car.owner_id

    def serialize(self):
        return {
            'id': self.id,
            'color': self.color,
            'model': self.model,
            'owner_id': self.owner_id
        }
