from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, redirect, render_template, request
from models.list import List
lists_blueprint = Blueprint('lists', __name__)


@lists_blueprint.route('/lists')
def lists():
    lists = List.query.all()
    return render_template('/lists/lists.jinja', lists=lists) 

@lists_blueprint.route('/lists/<id>')
def show_list(id):
    list = List.query.get(id)
    return render_template('/lists/show_list.jinja', list=list)