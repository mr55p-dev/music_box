from flask_server import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    user_id          =   db.Column(db.Integer(), primary_key = True)
    user_email       =   db.Column(db.String(100), unique = True, nullable = False)
    user_name        =   db.Column(db.String(100), nullable = False)
    user_password    =   db.Column(db.String(100), nullable = False)
    user_boxes       =   db.relationship('Box', backref = 'owner', lazy = True)

    def get_id(self):
        return self.user_id

class Box(db.Model):
    __tablename__ = 'boxes'

    box_id      =   db.Column(db.Integer(), primary_key = True)
    box_name    =   db.Column(db.String(100), unique=True, nullable = False)
    box_token   =   db.Column(db.String(100), unique=True, nullable = False)
    owner_id    =   db.Column(db.Integer(), db.ForeignKey('users.user_id'))

class Song(db.Model):
    __tablename__ = 'songs'

    song_id     =   db.Column(db.Integer(), primary_key = True)
    song_name   =   db.Column(db.String(100), unique = True, nullable = False)