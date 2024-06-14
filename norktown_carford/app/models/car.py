from .. import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(10), nullable=False)
    model = db.Column(db.String(15), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
