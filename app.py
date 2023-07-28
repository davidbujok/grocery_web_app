from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://davidbujok@localhost:5432/bread_butter"
app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from seed import seed
app.cli.add_command(seed)


from controllers.users_controllers import users_blueprint
from controllers.lists_controller import lists_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(lists_blueprint)
