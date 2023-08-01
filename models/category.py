from app import db

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    @classmethod
    def all_categories(cls):
        return db.session.scalars(db.select(cls))

    @classmethod
    def category_id(cls, name):
        category_id = db.session.scalar(
                        db.select(cls)
                        .where(cls.name == name)
                        )
        return category_id
