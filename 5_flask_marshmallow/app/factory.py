from flask import Flask
from .database import db
"""Import Marshmallow object from serializer.py"""
from .views.user import user_blueprint
from .views.post import post_blueprint


def create_app():
    """Flask Factory"""

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "" # Populate as required.

    db.init_app(app)
    # Initialize your Marshmallow object (ma.init_app())

    with app.app_context():
        db.create_all()
        db.session.commit()
    
    app.register_blueprint(user_blueprint)
    app.register_blueprint(post_blueprint)

    return app
