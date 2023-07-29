from app import db

class User(db.Model):

    __tablename__ = 'users'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    fullname: db.Mapped[str] = db.mapped_column(db.String(30))