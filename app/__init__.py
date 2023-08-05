from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'users.home'

    from app.controllers.users_controllers import users_blueprint
    from app.controllers.lists_controller import lists_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(lists_blueprint)

    from app.seed import seed
    app.cli.add_command(seed)

    return app

