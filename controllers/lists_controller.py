from app import db
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import select
from flask import Blueprint, redirect, render_template, request, url_for
from models.list import List
from models.item import Item
from models.user_list import UserList
from models.user import User
lists_blueprint = Blueprint('lists', __name__)


@lists_blueprint.route('/lists')
def lists():
    # lists = List.query.all()
    lists = db.session.scalars(db.select(List).order_by(List.name)).all()
    return render_template('/lists/lists.jinja', lists=lists) 

@lists_blueprint.route('/lists/<id>')
def show_list(id): 
    # list = List.query.get(id) 
    list = db.select(List).where(List.id == id)
    items = Item.query.all()
    on_list = db.session.scalars(
              db.select(UserList)
              .join(Item, UserList.item_list_id == Item.id)
              .where(UserList.user_list_id == id)
              .order_by(Item.name.asc())  
              )
    return render_template('/lists/show_list.jinja', list=list, items=items, on_list=on_list)

@lists_blueprint.route('/lists/<id>/search', methods=['GET', 'POST'])
def search_item(id):
    list = List.query.get(id)
    item_name_form = request.form['item']
    item = db.session.query(Item).filter_by(name=item_name_form).first()
    on_list = db.session.execute(
              db.select(UserList)
              .join(Item, UserList.item_list_id == Item.id)
              .where(UserList.user_list_id == id)
              .order_by(Item.name.asc())
              ).scalars()
    return render_template('/lists/search_item.jinja', list=list, item=item, on_list=on_list)

@lists_blueprint.route('/lists/<id>/add', methods=['POST'])
def add_item(id):
    list = List.query.get(id)
    item_name_form = request.form['item_name']
    item = db.session.query(Item).filter_by(name=item_name_form).first()
    user_list = UserList(user_list_id = list.id, item_list_id=item.id)
    db.session.add(user_list)
    db.session.commit()
    on_list = db.session.execute(db.select(UserList).where(UserList.user_list_id == id)).scalars()
    return render_template('/lists/search_item.jinja', list=list, item=item, on_list=on_list)