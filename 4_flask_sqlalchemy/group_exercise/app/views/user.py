from flask import Blueprint, request, jsonify
from app.models.user import User
from app.database import db


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/api/user", methods=["GET", "POST"])
def user_list():
    """Return all users and create new user."""
    pass
   


@user_blueprint.route("/api/user/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    """Return a single user from the database"""
    pass


@user_blueprint.route("/api/user/<int:user_id>", methods=["PATCH"])
def user_partial_update(user_id):
    """Perform partial update of user."""
    pass

        


@user_blueprint.route("/api/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete user from the database."""

    pass
