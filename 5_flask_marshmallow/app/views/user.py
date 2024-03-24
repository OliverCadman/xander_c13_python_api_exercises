from flask import Blueprint, request, jsonify
from app.models.user import User
from app.database import db


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/api/user", methods=["GET", "POST"])
def user_list():
    """Return all users from JSON Placeholder API"""

    if request.method == "GET":
        users = db.session.query(User).all()
        if len(users) <= 0:
            error_msg = "No results."
            return jsonify(msg=error_msg, status=200), 200

        # TODO: Replace with schema dump and return JSON.
        print(users)

        return "Retrieved users", 200

    else:

        # Get the JSON data from the request body.
        # Make sure to import 'request' from flask at the top.
        data = request.json

        # Try getting name, username, email and phone fields from our data, using dictionary indexing.
        try:
            name = data["name"]
            username = data["username"]
            email = data["email"]
            phone = data["phone"]

            # Create a new instance of User, passing in the required fields.
            new_user = User(name=name, username=username, email=email, phone=phone)

            # Add the new user to the database.
            db.session.add(new_user)

            # Commit the transaction. This is required to actually save the new user.
            db.session.commit()

            success_msg = "New user created."

            # Return a success message, the same data that was sent in the request, and a 201 (Created) response status.
            return jsonify(msg=success_msg, data=data, status_code=201), 201

        # If there is a KeyError, this means that either 'name', 'username', 'email' and 'phone' are not present
        # in the request data.
        except KeyError:

            error_msg = "Please specify fields <name>, <username>, <email> and <phone>"
            return jsonify(msg=error_msg, status_code=400)


@user_blueprint.route("/api/user/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    """Return a single user from JSON Placeholder API."""

    user = db.session.query(User).filter_by(id=user_id).first()
    if not user:
        error_msg = "User not found. Try a different ID."
        return jsonify(msg=error_msg, status=200), 200

    # TODO: Replace with schema dump and return as JSON.
    print(user)
    success_msg = f"User with id {user_id} retrieved."

    return success_msg, 200


@user_blueprint.route("/api/user/<int:user_id>", methods=["PATCH"])
def user_partial_update(user_id):
    """Perform partial update of user."""

    data = request.json

    user = db.session.query(User).filter_by(id=user_id).first()
    if not user:
        error_msg = "User does not exist. Try a different ID."
        return jsonify(msg=error_msg, status=400), 400

    try:
        for key, value in data.items():
            if not hasattr(user, key):
                raise ValueError
            else:
                setattr(user, key, value)
                db.session.commit()

        user = db.session.query(User).filter_by(id=user_id).first()

        # TODO: Replace with schema dump and return as JSON.
        success_msg = f"User with ID {user.id} updated."
        return success_msg, 200

    except ValueError:
        error_msg = "Error referencing columns with provided keys." \
                    " User object contains <id>, <name>, <username>, <email> and <phone>."
        return jsonify(msg=error_msg, status=400), 400


@user_blueprint.route("/api/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Perform DELETE request to delete user."""

    user = db.session.query(User).filter_by(id=user_id).first()
    msg = None
    if not user:
        msg = "User not found."
    else:
        db.session.delete(user)
        db.session.commit()

        msg = f"User with id {user_id} deleted."
    
    return msg, 200
