from app.database import db


class User(db.Model):
    """Model to represent a user record in database."""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    posts = db.relationship("Post", cascade="all, delete-orphan")

    def __init__(self, name, username, email, phone):
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"User {self.id}: {self.name}"
