from app import db
from models.list import List 
from models.item import Item
class UserList(db.Model):
    
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    user_list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    item_list_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    @classmethod
    def select_items_on_the_list(cls, list_id):
        on_list = db.session.scalars(
                    db.select(cls)
                    .join(Item, cls.item_list_id == Item.id)
                    .where(cls.user_list_id == list_id)
                    .order_by(Item.name.asc())
        )
        return on_list

    @classmethod
    def group_items_on_the_list(cls, list_id):
        on_list = cls.select_items_on_the_list(list_id)
        items_grouped = {}
        for user_list in on_list:
            if user_list.item.name not in items_grouped.keys():
                items_grouped[user_list.item.name] = 1
            else:
                items_grouped[user_list.item.name] += 1
        return items_grouped