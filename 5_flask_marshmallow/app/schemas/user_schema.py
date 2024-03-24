from app.serializer import ma
from app.models.user import User
from app.schemas.post_schema import PostSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the User SQLAlchemy object."""

    class Meta:
        # Provide the User model to serialize.
        model = User

        # Define the fields which will be in the output when User model is serialized.
        fields = ("id", "name", "username", "email", "phone", "posts")

    posts = ma.Nested(PostSchema, many=True)
