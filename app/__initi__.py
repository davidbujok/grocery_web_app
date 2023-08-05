from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from controllers.users_controllers import users_blueprint
    from controllers.lists_controller import lists_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(lists_blueprint)

    from seed import seed
    app.cli.add_command(seed)

    return app