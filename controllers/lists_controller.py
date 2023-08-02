from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for
from models.list import List
from models.item import Item
from models.user_list import UserList
from models.store import Store
from models.user import User
from models.category import Category


lists_blueprint = Blueprint('lists', __name__)


@lists_blueprint.route('/lists')
def lists():
    lists = List.select_all_lists()    
    return render_template('/lists/lists.jinja', lists=lists) 


@lists_blueprint.route('/lists/<user_id>/<list_id>')
def show_list(user_id, list_id): 

    items = Item.select_all_items()
    categories = Category.select_all_categories()
    list = List.select_the_list(list_id)
    on_list = UserList.group_items_on_the_list(list_id)
    user = User.select_user_by_id(user_id)

    return render_template('/lists/show_list.jinja', items=items, categories=categories, list=list, on_list=on_list, user=user)


@lists_blueprint.route('/lists/<list_id>/search', methods=['GET', 'POST'])
def search_item(list_id):

    item_name = request.form['item']
    list = List.select_the_list(list_id)
    user = User.match_user_with_list(list_id) 
    item = Item.select_search_item(item_name)
    on_list = UserList.group_items_on_the_list(list_id)
    items = Item.select_all_items()

    return render_template('/lists/search_item.jinja', list=list, item=item, on_list=on_list, items=items, user=user)


@lists_blueprint.route('/lists/<id>/add', methods=['POST'])
def add_item(id):

    item_name = request.form['item_name']
    item = Item.select_search_item(item_name)
    items = Item.select_all_items()
    list = List.select_the_list(id)
    UserList.add_new_item_to_the_list(list.id, item.id)
    on_list = UserList.group_items_on_the_list(list.id)
    user = User.match_user_with_list(list.id)
#     stores = Store.select_user_stores(user.id)

    return render_template('/lists/search_item.jinja', list=list, item=item, on_list=on_list, items=items, user=user)

    # removed stores=stores from return statement

@lists_blueprint.route('/lists/<list_id>/<user_id>/delete', methods=['POST'])
def delete_item(list_id, user_id):
    item_name = request.form['item_name']
    print(item_name)
    item = Item.select_search_item(item_name)
#     list = List.select_the_list(list_id)
    UserList.delete_item_on_the_list(list_id, item.id)    
    return redirect(url_for('lists.show_list', user_id=user_id, list_id=list_id))