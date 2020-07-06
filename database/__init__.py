from app import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    