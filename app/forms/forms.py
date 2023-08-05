from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired

class CreateList(FlaskForm):
    name = StringField('List', validators=[DataRequired()])
    budget = FloatField('Budget', validators=[DataRequired()])
    submit = SubmitField('Create')


class CreateItem(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    item_category = SelectField(u'Category', coerce=int)
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add')