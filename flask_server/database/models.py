from flask_server import db
from flask_login import UserMixin

songs_on_box = db.Table('songs_on_box', 
    db.Column('songID', db.Integer(), db.ForeignKey('songs.songID')),
    db.Column('boxID', db.Integer(), db.ForeignKey('boxes.boxID'))
)

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
    songs = db.relationship('Song', secondary=songs_on_box, backref=db.backref('boxes'))

    def __repr__(self):
        return f"<Box {self.boxName}"

class Song(db.Model):
    __tablename__ = "songs"

    songID = db.Column(db.Integer, primary_key=True)
    songName = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f"<Song {self.songName}"