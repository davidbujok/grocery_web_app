from app import db
from models.list import List 
from models.item import Item
class UserList(db.Model):
    
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    user_list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    item_list_id = db.Column(db.Integer, db.ForeignKey('items.id'))