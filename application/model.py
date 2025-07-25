from application.database import db
from sqlalchemy import Enum


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pin_code = db.Column(db.Integer, nullable=False)
    role = db.Column(Enum("A", "U", name="role"), nullable=False, default="U")

    def __repr__(self):
        return {"username": self.username, "fullname": self.fullname}
