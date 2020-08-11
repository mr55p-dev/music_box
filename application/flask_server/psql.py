from flask import Blueprint
from . import db, db_url
from .models import User
import click

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
    from time import time
    testQuery = User(
        email=f"testMail{str(time())}",
        name="testName",
        password="testPassword"
    )
    db.session.add(testQuery)
    db.session.commit()
    print("Complete")

@psql.cli.command("query")
@click.argument("name")
def queryDB(name):
    res = User.query.filter_by(name=name).all()
    if not res:
        print("No matches.")
    else:
        print(f"{len(res)} result(s)")
        [print(i.name) for i in res]