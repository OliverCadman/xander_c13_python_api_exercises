from app.database import db


class Post(db.Model):
    """Model to represent a post in the database."""

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user = db.relationship("User", back_populates="posts")

    def __init__(self, user_id, title, body):
        self.user_id = user_id
        self.title = title
        self.body = body

    def __str__(self):
        return f"Post by user {self.user_id}: {self.title}"
