from application.database import db
from sqlalchemy import text


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pin_code = db.Column(db.Integer, nullable=False)
    role = db.Column(db.Enum("A", "U", name="role"), nullable=False, default="U")

    reserve_parking_spots = db.relationship(
        "ReserveParkingSpot", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"username: {self.email}, fullname: {self.fullname}"


class ParkingLot(db.Model):
    __tablename__ = "parking_lots"
    id = db.Column(db.Integer, primary_key=True)
    prime_location = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pin_code = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    max_spots = db.Column(db.Integer, nullable=False)

    parking_spots = db.relationship(
        "ParkingSpot", backref="lot", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"(prime_location:{self.prime_location}, address:{self.address}, pin_code:{self.pin_code}, price:{self.price}, max_spots:{self.max_spots})"


class ParkingSpot(db.Model):
    __tablename__ = "parking_spots"
    id = db.Column(db.Integer, primary_key=True)
    lot_id = db.Column(
        db.Integer,
        db.ForeignKey("parking_lots.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    status = db.Column(db.Enum("A", "O", name="status"), nullable=False, default="A")
    reserve_parking_spots = db.relationship("ReserveParkingSpot", backref="spot")

    def __repr__(self):
        return f"(id:{self.id} ,lot_id:{self.lot_id}, status:{self.status})"


class ReserveParkingSpot(db.Model):
    __tablename__ = "reserve_parking_spots"
    id = db.Column(db.Integer, primary_key=True)
    spot_id = db.Column(db.Integer, db.ForeignKey("parking_spots.id"), nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    vehicle_number = db.Column(db.String(100), nullable=False)
    parking_timestamp = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=text("now()")
    )
    leaving_timestamp = db.Column(db.DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"(id:{self.id}, spot_id:{self.spot_id}, user_id:{self.user_id}, vehicle_number:{self.vehicle_number}, parking_timestamp: {self.parking_timestamp}, leaving_timestamp:{self.leaving_timestamp})"
