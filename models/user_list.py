from app import db
from models.list import List 
from models.item import Item
class UserList(db.Model):
    
    __tablename__ = 'user_list'

    id = db.Column(db.Integer, primary_key=True)
    user_list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    item_list_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    @classmethod
    def add_new_item_to_the_list(cls, list_id, item_id):
        new_item = UserList(user_list_id=list_id, item_list_id=item_id)
        db.session.add(new_item)
        db.session.commit()

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

    @classmethod
    def delete_item_on_the_list(cls, list_id, item_id):
        entry_to_delete = db.session.scalar(
                            db.select(cls)
                            .where((cls.user_list_id == list_id) &
                            (cls.item_list_id == item_id))
        )
        db.session.delete(entry_to_delete)
        db.session.commit() 