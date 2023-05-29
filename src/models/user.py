from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
