from app import db

class Item(db.Model):

    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42))
    category = db.Column(db.String(48))
    price = db.Column(db.Float)
    user_list = db.relationship('UserList', backref='item') 


    @classmethod
    def return_all_categories(cls):
        categories = db.session.scalars(
                    db.select(cls.category)
                    )
        unique = []
        for category in categories:
            if category not in unique:
                unique.append(category)
        return unique
