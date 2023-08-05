from flask_wtf import FlaskForm
from app import db
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired
from app.models.category import Category

class CreateList(FlaskForm):
    name = StringField('List', validators=[DataRequired()])
    budget = FloatField('Budget', validators=[DataRequired()])
    submit = SubmitField('Create')


class CreateItem(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    item_category = SelectField(u'Category', coerce=int)
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add')