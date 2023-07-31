from app import db

class Category(db.Model):

    __tablename__ = 'categories'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String(30))
    