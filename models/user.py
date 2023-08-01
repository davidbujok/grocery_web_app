from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(30))
    lists = db.relationship('List', backref='user')
    stores = db.relationship('Store', backref='user')

    @classmethod
    def user_id(cls, id):
        user_id = db.session.scalar(
                    db.select(cls)
                    .where(cls.id == id)
                    )
        return user_id