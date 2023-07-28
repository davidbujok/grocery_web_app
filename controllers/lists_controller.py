from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, redirect, render_template, request
from models.list import List
from models.item import Item
lists_blueprint = Blueprint('lists', __name__)


@lists_blueprint.route('/lists')
def lists():
    lists = List.query.all()
    return render_template('/lists/lists.jinja', lists=lists) 

@lists_blueprint.route('/lists/<id>')
def show_list(id):
    list = List.query.get(id) 
    items = Item.query.all()
    return render_template('/lists/show_list.jinja', list=list, items=items)

@lists_blueprint.route('/lists/<id>/search', methods=['POST'])
def search_item(id):
    list = List.query.get(id)
    item_name_form = request.form['item']
    item = db.session.query(Item).filter_by(name=item_name_form).first()
    return render_template('/lists/search_item.jinja', list=list, item=item)
