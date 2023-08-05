from app import db, login
from app.models.list import List
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(64)) 
    password_hash = db.Column(db.String(128))
    lists = db.relationship('List', backref='user', cascade="all, delete-orphan")
    stores = db.relationship('Store', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
        
        

    @classmethod
    def select_all_users(cls):
        users = db.session.scalars(
                db.select(cls)
                )
        return users

    @classmethod
    def select_user_by_id(cls, user_id):
        user = db.session.scalar(
                    db.select(cls)
                    .where(cls.id == user_id)
                    )
        return user

    @classmethod
    def match_user_with_list(cls, list_id):
        user = db.session.scalar(
                db.select(cls)
                .join(List, cls.id == List.user_id)
                )
        return user
# fix that for stores variable in add_item > lists blueprint

    @classmethod
    def select_user_by_name(cls, name):
        user = db.session.scalar(
                db.select(cls)
                .where(cls.username == name)
                )
        return user

    @classmethod
    def delete_user_by_id(cls, user):
        db.session.delete(user)
        db.session.commit()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))