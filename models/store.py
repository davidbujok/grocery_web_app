from app import db

class Store(db.Model):

    __tablename__ = 'stores'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String(30))
    address: db.Mapped[str] = db.mapped_column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    @classmethod
    def select_user_stores(cls, user_id):
        stores = db.session.scalars(
                db.select(cls)
                .where(cls.user_id == user_id)
                )
        return stores

    @classmethod
    def add_new_store(cls, layout, address, user_id):
        new_store = Store(name=layout, address=address, user_id=user_id)
        db.session.add(new_store)
        db.session.commit()

    @classmethod
    def select_store_by_name(cls, store_name):
        store = db.session.scalar(
                db.select(cls)
                .where(cls.name == store_name)
                )
        return store