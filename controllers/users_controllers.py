from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app import db
from models.user import User
from models.item import Item
from models.category import Category  
from models.list import List 
from models.user_layouts import UserLayouts
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
    user = User.user_id(id)
    return redirect(url_for('lists.show_list', userid=user.id, id=new_list.id))


@users_blueprint.route('/user/<id>/create_layout', methods=['GET', 'POST'])
def create_layout(id):
    user = User.user_id(id)
    if request.method == 'POST':
        layout = request.form['store']
        address= request.form['address']
        new_store = Store(name=layout, address=address, user_id=user.id)
        db.session.add(new_store)
        db.session.commit()
    categories = Item.return_all_categories()
    return render_template('/users/create_layout.jinja', categories=categories, user=user)