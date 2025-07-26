from flask import Flask
from application.database import db
from application.model import User, ParkingLot, ParkingSpot, ReserveParkingSpot

app = Flask(__name__)
app.config["SECRET_KEY"] = "24f1000209"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///app.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def seed_initial_data():
    existing_lot = ParkingLot.query.first()
    if existing_lot:
        return print("Initial data exists in Database.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
