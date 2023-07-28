from app import db

class List(db.Model):

    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(48))
    budget = db.Column(db.Float)