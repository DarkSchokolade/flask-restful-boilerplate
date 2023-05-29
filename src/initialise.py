import os

from flask import Flask
from flask_cors import CORS

from extensions import db

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database.sqlite"

db.init_app(app)


def initialize_database():
    with app.app_context():
        db.create_all()
