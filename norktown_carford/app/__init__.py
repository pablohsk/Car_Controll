from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .views.car_view import car_bp
    from .views.owner_view import owner_bp
    from .views.user_view import user_bp

    app.register_blueprint(car_bp, url_prefix='/cars')
    app.register_blueprint(owner_bp, url_prefix='/owners')
    app.register_blueprint(user_bp, url_prefix='/users')

    return app
