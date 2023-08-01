from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(30))
    lists = db.relationship('List', backref='user', cascade="all, delete-orphan")
    stores = db.relationship('Store', backref='user')

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
                .where(cls.id == list_id)
                )
        return user

    @classmethod
    def select_user_by_name(cls, name):
        user = db.session.scalar(
                db.select(cls)
                .where(cls.fullname == name)
                )
        return user

    @classmethod
    def delete_user_by_id(cls, user):
        db.session.delete(user)
        db.session.commit()
