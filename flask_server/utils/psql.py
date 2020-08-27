from flask import Blueprint, current_app
from flask_server import db
# from flask_server.database.models import User, Song

psql = Blueprint("psql", __name__)


@psql.cli.command("reset")
def resetDB():
    from sqlalchemy_utils import database_exists, create_database, drop_database
    # print(db_url)
    if database_exists(current_app.config["SQLALCHEMY_DATABASE_URI"]):
        print('Deleting old database')
        drop_database(current_app.config["SQLALCHEMY_DATABASE_URI"])

    if not database_exists(current_app.config["SQLALCHEMY_DATABASE_URI"]):
        print('Rebuilding database')
        create_database(current_app.config["SQLALCHEMY_DATABASE_URI"])

    print('Creating tables')
    db.create_all()
    db.session.commit()
    print('Complete')
