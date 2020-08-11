from os import environ as env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate_obj = Migrate()

def create_app():
    # Create an application object
    app = Flask(__name__)

    # Load the database environment variables
    try:
        db_info = [
            env["POSTGRES_USER"],
            env["POSTGRES_PW"],
            env["POSTGRES_URL"],
            env["POSTGRES_DB"]
        ]
    except Exception as e:
        print("Error configuring one or more enviornment variables.")
        raise 

    global db_url
    db_url = f'postgresql+psycopg2://{db_info[0]}:{db_info[1]}@{db_info[2]}/{db_info[3]}'

    # Configure the application variables for SQLAlchemy and initalise the database

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initalise plugins
    db.init_app(app)
    migrate_obj.init_app(app, db)

    # Register the applications routes as blueprints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .psql import psql as psql_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(psql_blueprint)
    
    return app
