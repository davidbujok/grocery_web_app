from app import db

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    @classmethod
    def select_all_categories(cls):
        return db.session.scalars(db.select(cls))

    @classmethod
    def select_category_by_name(cls, category_name):
        category = db.session.scalar(
                        db.select(cls)
                        .where(cls.name == category_name)
                        )
        return category
