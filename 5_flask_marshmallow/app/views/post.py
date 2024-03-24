from flask import Blueprint, jsonify, request
from app.database import db
from app.models.post import Post
from app.models.user import User
from app.schemas.post_schema import PostSchema


post_blueprint = Blueprint("post", __name__)


@post_blueprint.route("/api/post", methods=["GET", "POST"])
def post_list():
    """Return all users from JSON Placeholder API"""

    if request.method == "GET":
        posts = db.session.query(Post).all()
        if len(posts) <= 0:
            error_msg = "No results."
            return jsonify(msg=error_msg, status=200), 200

        # TODO: Replace with schema dump and return JSON.
        schema = PostSchema(many=True)
        data = schema.dump(posts)

        return jsonify(
            data=data,
            status=200
        ), 200

    else:
        data = request.json

        try:
            user_id = data["user_id"]
            user = db.session.query(User).filter_by(id=user_id).first()
            # .first() returns an object
            # .all() returns a list of objects. This is iterable.
            if not user:
                error_msg = "User not found. Please try a different id."
                return jsonify(msg=error_msg, status=400), 400

            title = data["title"]
            body = data["body"]

            new_post = Post(user_id=user.id, title=title, body=body)
            db.session.add(new_post)
            db.session.commit()

            success_msg = "New post created."
            return jsonify(data=data, msg=success_msg, status=201), 201
        except KeyError:
            error_msg = "Please specify <user_id>, <title>, and <body>."
        return jsonify(msg=error_msg, status=400), 400


@post_blueprint.route("/api/post/<int:post_id>", methods=["GET"])
def get_single_post(post_id):
    """Return a single user from JSON Placeholder API."""

    post = db.session.query(Post).filter_by(id=post_id).first()
    if not post:
        error_msg = "User not found. Try a different ID."
        return jsonify(msg=error_msg, status=200), 200

    # TODO: Replace with schema dump and return as JSON.
    schema = PostSchema(many=False)
    data = schema.dump(post)
    return jsonify(
        data=data,
        status=200,
    ), 200


@post_blueprint.route("/api/post/<int:post_id>", methods=["PATCH"])
def post_partial_update(post_id):
    """Perform partial update of post."""

    data = request.json

    post = db.session.query(Post).filter_by(id=post_id).first()
    if not post:
        error_msg = "User does not exist. Try a different ID."
        return jsonify(msg=error_msg, status=400), 400

    try:
        for key, value in data.items():
            if not hasattr(post, key):
                raise ValueError
            else:
                setattr(post, key, value)
                db.session.commit()

        updated_post = db.session.query(User).filter_by(id=post_id).first()

        schema = PostSchema(many=False)
        schema.dump(updated_post)

        return jsonify(
            data=updated_post,
            status=200
        )

    except ValueError:
        error_msg = "Error referencing columns with provided keys." \
                    " User object contains <id>, <name>, <username>, <email> and <phone>."
        return jsonify(msg=error_msg, status=400), 400


@post_blueprint.route("/api/post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    """Perform DELETE request to delete user."""

    post = db.session.query(Post).filter_by(id=post_id).first()
    msg = None
    if not post:
        msg = "Post not found."
    else:
        db.session.delete(post)
        db.session.commit()

        msg = f"Post with id {post_id} deleted."
    
    return msg, 200
