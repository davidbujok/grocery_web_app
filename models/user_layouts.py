from app import db

class UserLayouts(db.Model):

    __tablename__ = 'layouts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    @classmethod
    def create_new_layout(cls, store_id, category_id):
        new_layout = UserLayouts(user_store_id = store_id, category_id = category_id)
        db.session.add(new_layout)
        db.session.commit()