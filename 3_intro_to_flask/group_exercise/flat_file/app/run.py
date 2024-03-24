"""
This file contains the 'views' of the Flask application.

Views are like functions, but they are turned into functions that
can be called through a browser or 'requests' library, by adding a python
decorator provided by the Flask library.
"""


def user_group():
    """GET a list of users or POST a single user."""
    pass


def user_item(user_id):
    """GET a user by ID."""
    pass


def post_group():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
