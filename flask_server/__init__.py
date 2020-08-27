from flask_server.utils.helperClasses import ThreadHandler
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
application_log = logging.getLogger()
env = os.getenv
th = ThreadHandler()


def create_app():
    # Create an application object
    app = Flask(__name__)

    # Load the database environment variables
    db_info = [
        env("POSTGRES_USER"),
        env("POSTGRES_PW"),
        env("POSTGRES_URL"),
        env("POSTGRES_DB"),
    ]

    # This is sloppy, change it soon.
    db_url = f'postgresql+psycopg2://{db_info[0]}:{db_info[1]}@{db_info[2]}/{db_info[3]}'

    # Configure the application variables for SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = env("SECRET_KEY")
    app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), 'flask_server/uploads/')
    app.config["ALLOWED_FILETYPES"] = {"mp3"}

    # Initalise plugins
    application_log.setLevel(logging.DEBUG)
    logging.basicConfig(filename=os.path.join(os.getcwd(), 'flask_server/logs/main.log'))
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # TEST
    from .database.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register the applications routes as blueprints
    from .routes.auth import auth as auth_blueprint
    from .routes.main import main as main_blueprint
    from .routes.product import product as prod_blueprint
    from .utils.psql import psql as psql_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(prod_blueprint)
    app.register_blueprint(psql_blueprint)

    return app
