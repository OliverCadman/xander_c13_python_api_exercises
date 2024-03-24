from flask import Blueprint, jsonify, request
from app.database import db
from app.models.post import Post
from app.models.user import User


post_blueprint = Blueprint("post", __name__)


@post_blueprint.route("/api/post", methods=["GET", "POST"])
def post_group():
    """
    Return all posts and create new post.
    """
    pass


@post_blueprint.route("/api/post/<int:post_id>", methods=["GET"])
def get_single_post(post_id):
    """Return a single post from the database."""
    pass


@post_blueprint.route("/api/post/<int:post_id>", methods=["PATCH"])
def post_partial_update(post_id):
    """Perform partial update of post."""
    pass


@post_blueprint.route("/api/post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    """Remove post from database."""
    pass
