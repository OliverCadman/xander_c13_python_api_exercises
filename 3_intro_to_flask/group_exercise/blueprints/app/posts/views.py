from flask import Blueprint, request


post_blueprint = Blueprint("posts", __name__)


@post_blueprint.route("/api/posts", methods=["GET", "POST"])
def user_group():
    """GET a list of posts or POST a single post."""
    if request.method == "GET":
        return "Getting users!"
    else:
        return "Posting user!"
