from ..models.user import User
from .. import db

def create_user(data):
    if User.query.filter_by(username=data['username']).first() is not None:
        return None
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None
