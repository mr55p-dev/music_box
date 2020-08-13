from flask_server import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(1000))

    def __repr__(self):
        return f"<User {self.name}>"