from flask_restful import Resource

from models.user import User
from extensions import db


class UserHandler(Resource):
    def get(self):
        user = User(username="Bunny", email="Bun@gmail.com")
        db.session.add(user)
        db.session.commit()
        return "user created", 201
