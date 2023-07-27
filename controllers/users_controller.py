from flask import Blueprint, render_template, redirect, url_for

users_controller = Blueprint('users_controller', __name__)


@users_controller.route('/')
def home():
    return render_template('index.jinja')