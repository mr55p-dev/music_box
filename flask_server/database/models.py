from flask_server import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(150), nullable=True)


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    artist = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(400), unique=False, nullable=True)
    path = db.Column(db.String(100), unique=True, nullable=False)
