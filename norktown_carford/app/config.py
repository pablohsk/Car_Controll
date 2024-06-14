import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@db:5432/norktown_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.urandom(24)
