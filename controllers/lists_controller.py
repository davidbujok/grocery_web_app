from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, redirect, render_template, request, url_for
from models.list import List
from models.item import Item
from models.user_list import UserList
from models.user import User
lists_blueprint = Blueprint('lists', __name__)


@lists_blueprint.route('/lists')
def lists():
    lists = db.session.execute(
            db.select(List)
            ).scalars()
    return render_template('/lists/lists.jinja', lists=lists) 


@lists_blueprint.route('/lists/<id>')
def show_list(id): 
    list = db.session.scalar(
            db.select(List)
            .where(List.id == id)
            )
    items = db.session.scalars(
            db.select(Item)
            )
    on_list = db.session.scalars(
              db.select(UserList)
              .join(Item, UserList.item_list_id == Item.id)
              .where(UserList.user_list_id == id)
              .order_by(Item.name.asc())
              )
    return render_template('/lists/show_list.jinja', list=list, items=items, on_list=on_list)


@lists_blueprint.route('/lists/<id>/search', methods=['GET', 'POST'])
def search_item(id):
    item_name_form = request.form['item']
    list = db.session.scalar(
            db.select(List)
            .where(List.id == id)
            )
    item = db.session.scalar(
            db.select(Item)
            .where(Item.name == item_name_form)
            )
    on_list = db.session.scalars(
                db.select(UserList)
                .join(Item, UserList.item_list_id == Item.id)
                .where(UserList.user_list_id == id)
                .order_by(Item.name.asc())
                )
    return render_template('/lists/search_item.jinja', list=list, item=item, on_list=on_list)


@lists_blueprint.route('/lists/<id>/add', methods=['POST'])
def add_item(id):
    item_name_form = request.form['item_name']
    list = db.session.scalar(
            db.select(List)
            .where(List.id == id)
            )
    item = db.session.scalar(
            db.select(Item)
            .where(Item.name == item_name_form)
            )
    user_list = UserList(user_list_id = list.id, item_list_id=item.id)
    db.session.add(user_list)
    db.session.commit()

    on_list = db.session.scalars(
                db.select(UserList)
                .where(UserList.user_list_id == id)
                )
    return render_template('/lists/search_item.jinja', list=list, item=item, on_list=on_list)