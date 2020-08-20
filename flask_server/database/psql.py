import click
from flask import Blueprint
from flask_server import db, db_url
from flask_server.database.models import User, Song

psql = Blueprint("psql", __name__)

@psql.cli.command("reset")
def resetDB():
    from sqlalchemy_utils import database_exists, create_database, drop_database
    # print(db_url)
    if database_exists(db_url):
        print('Deleting old database')
        drop_database(db_url)

    if not database_exists(db_url):
        print('Rebuilding database')
        create_database(db_url)
        
    print('Creating tables')
    db.create_all()
    db.session.commit()
    print('Complete')

@psql.cli.command("test")
def testDB():
    newSong = Song(
        name = "Song",
        artist = "Artist",
        description = "Lorem ipsum.",
        path = "/path/"
    )


    db.session.add(newSong)
    db.session.commit()
    print("Complete")
