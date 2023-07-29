from flask import Flask, Blueprint, render_template
from app import db
from models.user import User
from models.item import Item
from models.list import List 
from models.user_list import UserList

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/')
def home():
    users = db.session.scalars(db.select(User))
    return render_template('index.jinja', users=users)

