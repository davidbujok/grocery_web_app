from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgresql://davidbujok@localhost:5432/bread_and_butter'
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.users_controller import users_controller
app.register_blueprint(users_controller)




if __name__ == '__main__':
    app.run(debug=True)
