from app import db

class Item(db.Model):

    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42))
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.Float)
    user_list = db.relationship('UserList', backref='item') 

    @classmethod
    def select_all_items(cls):
        item = db.session.scalars(
                db.select(cls)
                )
        return item
 
    @classmethod
    def select_search_item(cls, item_name):
        item = db.session.scalar(
            db.select(cls)
            .where(cls.name == item_name)
            )
        return item