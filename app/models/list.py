from app import db

class List(db.Model):

    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(48))
    budget = db.Column(db.Float)
    user_lists = db.relationship('UserList', backref='list')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',  ondelete="CASCADE")) 

    @classmethod
    def select_all_lists(cls):
        lists = db.session.scalars(
                db.select(cls)
                )
        return lists

    @classmethod
    def select_the_list(cls, list_id):
        list = db.session.scalar(
                db.select(cls)
                .where(cls.id == list_id)
                )
        return list

    @classmethod
    def delete_the_list(cls, list):
        db.session.delete(list)
        db.session.commit()
        
    @classmethod
    def add_new_list(cls, name, budget, user_id):
        new_list = List(name=name, budget=budget, user_id=user_id)
        db.session.add(new_list)
        db.session.commit()
        return new_list