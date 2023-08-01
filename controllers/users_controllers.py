from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app import db
from models.user import User
from models.user_layouts import UserLayouts
from models.category import Category
from models.list import List 
from models.store import Store

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/')
def home():
    users = User.select_all_users()
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


@users_blueprint.route('/delete/<user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.select_user_by_id(user_id)
    User.delete_user_by_id(user)
    return redirect(url_for('users.home'))
   


@users_blueprint.route('/user/<name>')
def user(name):
    user = User.select_user_by_name(name)
    lists = List.select_all_lists()
    return render_template('/users/user.jinja', user=user, lists=lists, user_lists=user.lists)


@users_blueprint.route('/user/<user_id>/add_list', methods=['POST', 'GET'])
def add_list(user_id):
    name = request.form['name']
    budget = request.form['budget']
    new_list = List.add_new_list(name, budget, user_id)
    return redirect(url_for('lists.show_list', user_id=user_id, list_id=new_list.id))


@users_blueprint.route('/delete/<user_id>/list/<list_id>', methods=['POST'])
def delete_list(user_id, list_id):
    list = List.select_the_list(list_id)
    List.delete_the_list(list)
    user = User.select_user_by_id(user_id)
    return redirect(url_for('users.user', name=user.fullname))
    


@users_blueprint.route('/user/<user_id>/create_layout', methods=['GET', 'POST'])
def create_layout(user_id):
    user = User.select_user_by_id(user_id)
    categories = Category.select_all_categories()
    if request.method == 'POST':
        layout = request.form['store']
        address= request.form['address']
        Store.add_new_store(layout, address, user_id)
    stores = Store.select_user_stores(user_id)
    return render_template('/users/create_layout.jinja', categories=categories, user=user, stores=stores)


@users_blueprint.route('/user/<user_id>/create_layout/sort', methods=['GET', 'POST'])
def create_sort_method(user_id):
    store_name = request.form['store']
    category_name = request.form['category']
    store = Store.select_store_by_name(store_name)
    category = Category.select_category_by_name(category_name)
    UserLayouts.create_new_layout(store.id, category.id)
    user = User.select_user_by_id(user_id)
    categories = Category.select_all_categories()
    return render_template('/users/create_sort_method.jinja', store=store, user=user, categories=categories)

