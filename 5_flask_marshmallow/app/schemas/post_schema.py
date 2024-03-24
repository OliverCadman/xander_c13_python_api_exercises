from app.models.post import Post
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class PostSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the Post model."""

    class Meta:
        model = Post
        fields = ("id", "user_id", "title", "body")
