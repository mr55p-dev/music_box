from os import environ as env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

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

    # This is sloppy, change it soon.
    global db_url
    db_url = f'postgresql+psycopg2://{db_info[0]}:{db_info[1]}@{db_info[2]}/{db_info[3]}'

    # Configure the application variables for SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = env["SECRET_KEY"]
    
    # Initalise plugins
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .database.models import User
    @login_manager.user_loader
    def load_user(userID):
        return User.query.get(int(userID))


    # Register the applications routes as blueprints
    from .routes.auth import auth as auth_blueprint
    from .routes.main import main as main_blueprint
    from .database.psql import psql as psql_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(psql_blueprint)
    
    return app
