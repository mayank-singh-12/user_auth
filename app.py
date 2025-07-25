from flask import Flask
from application.database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "24f1000209"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

from application.controller import root

app.register_blueprint(root)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        from application.model import User

        admin = User.query.filter_by(role="A").first()
        if not admin:
            admin = User(
                email="admin@gmail.com",
                password="admin123",
                fullname="admin",
                address="iitm",
                pin_code="111222",
                role="A",
            )
            db.session.add(admin)
            db.session.commit()
    app.run(host="0.0.0.0", debug=True, port=8080)
