from app import db
from models.store import Store
from models.user import User

class UserLayouts(db.Model):

    __tablename__ = 'layouts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))


    # @classmethod
    # def user_layouts(cls, user_id):
    #     layouts = db.session.scalars(
    #                 db.select(cls)
    #                 .join(Store, cls.user_store_id == Store.id)
    #                 .join(User, Store.user_id == user_id)
    #                 .where(Store.user_id == user_id)
    #                 )
    #     return layouts