from app import db

class UserLayouts(db.Model):

    __tablename__ = 'layouts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))