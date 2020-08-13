from flask_server import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(1000))
    boxes = db.relationship('Box', backref=db.backref('owner'), lazy=False)

    def __repr__(self):
        return f"<User {self.name}>"

class Box(db.Model):
    __tablename__ = "boxes"

    boxID = db.Column(db.Integer, primary_key=True)
    boxName = db.Column(db.String(100), unique=True)
    boxToken = db.Column(db.String(100))
    userID = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Box {self.boxName}"