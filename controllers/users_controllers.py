from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app import db
from models.user import User
from models.item import Item
from models.list import List 
from models.store import Store
from models.user_list import UserList

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/')
def home():
    users = db.session.scalars(db.select(User))
    return render_template('index.jinja', users=users)


@users_blueprint.route('/add/user', methods=['GET', 'POST'])
def add_user():
    
    if request.method == 'POST':
        full_name = request.form['fullname']
        new_user = User(fullname=full_name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.home'))
    return render_template('/users/add_user.jinja')

    
@users_blueprint.route('/user/<name>')
def user(name):
    user_is = db.session.scalar(
            db.select(User)
            .where(User.fullname==name)
            )
    lists = db.session.execute(
            db.select(List)
            ).scalars()
    user_lists = user_is.lists
    return render_template('/users/user.jinja', user=user_is, lists=lists, user_lists=user_lists)


@users_blueprint.route('/user/<id>/add_list', methods=['POST', 'GET'])
def add_list(id):

    name = request.form['name']
    budget = request.form['budget']
    new_list = List(name=name, budget=budget, user_id=id)
    db.session.add(new_list)
    db.session.commit()
    return redirect(url_for('lists.show_list', id=new_list.id))


@users_blueprint.route('/user/<id>/create_layout')
def create_layout(id):
    categories = Item.return_all_categories()
    user_is = db.session.scalar(
            db.select(User)
            .where(User.fullname==name)
            )
    return render_template('/users/create_layout.jinja', categories=categories, user=user_is)