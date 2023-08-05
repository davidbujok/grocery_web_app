from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from app import db
from flask_login import current_user, login_user, logout_user, login_required
from app.models.user import User
from app.models.item import Item
from app.models.user_layouts import UserLayouts
from app.models.category import Category
from app.models.list import List 
from app.models.store import Store
from app.forms.forms import CreateList, CreateItem
from app.forms.login import LoginForm
from app.forms.registration import RegistrationForm
from werkzeug.urls import url_parse

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('users.user', name=current_user.username))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() 
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('users.home'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('users.home')
        return redirect(url_for('users.user', name=user.username))
    return render_template('index.jinja', form=form)


@users_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.home'))

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data) 
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.home'))
    return render_template('/users/register.jinja', title='Register', form=form)


@users_blueprint.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        full_name = request.form['username']
        new_user = User(username=full_name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.home'))
    return render_template('/users/add_user.jinja')


@users_blueprint.route('/delete/<user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.select_user_by_id(user_id)
    User.delete_user_by_id(user)
    return redirect(url_for('users.home'))
   


@users_blueprint.route('/user/<name>', methods=['GET', 'POST'])
@login_required
def user(name):
    # user = User.select_user_by_name(name)
    lists = List.select_all_lists()
    form = CreateList()
    return render_template('/users/user.jinja', lists=lists, form=form)


@users_blueprint.route('/user/<user_id>/add_list', methods=['POST', 'GET'])
def add_list(user_id):
    user = User.select_user_by_id(user_id)
    # name = request.form['name']
    # budget = request.form['budget']
    form = CreateList()
    if form.validate_on_submit():
        new_list = List.add_new_list(form.name.data, form.budget.data, user_id)
        return redirect(url_for('lists.show_list', user_id=user_id, list_id=new_list.id))
    return redirect(url_for('users.user', name=user.username))




@users_blueprint.route('/delete/<user_id>/list/<list_id>', methods=['POST'])
def delete_list(user_id, list_id):
    list = List.select_the_list(list_id)
    List.delete_the_list(list)
    user = User.select_user_by_id(user_id)
    return redirect(url_for('users.user', name=user.username))
    


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

@users_blueprint.route('/add_item', methods=['GET', 'POST'])
def add_new_item_to_database():
    categories = Category.select_all_categories()
    form = CreateItem(obj=categories) 
    form.item_category.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    if form.validate_on_submit():
        if Item.select_search_item(form.name.data) == None:
            new_item = Item(name=form.name.data, category=form.item_category.data, price=form.price.data)
            db.session.add(new_item)
            db.session.commit()
        else:
            flash("You already have this product :)")
    return render_template('/items/add_item.jinja', categories=categories, form=form)