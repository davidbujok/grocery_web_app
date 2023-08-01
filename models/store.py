from app import db

class Store(db.Model):

    __tablename__ = 'stores'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String(30))
    address: db.Mapped[str] = db.mapped_column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    @classmethod
    def user_stores(cls, user_id):
        stores = db.session.scalars(
                db.select(cls)
                .where(cls.user_id == user_id)
                )
        return stores

    
