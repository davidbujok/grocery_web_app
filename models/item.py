from app import db

class Item(db.Model):

    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42))
    category = db.Column(db.String(48))
    price = db.Column(db.Float)
    user_list = db.relationship('UserList', backref='item') 
