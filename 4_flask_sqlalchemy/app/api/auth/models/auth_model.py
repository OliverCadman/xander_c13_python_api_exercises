from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import NoResultFound, OperationalError, IntegrityError
from app.api.common.models.db_interface import DBInterface

import time


class AuthUser(db.Model):
    """Model to represent an auth user in the DB."""
    __tablename__ = "auth_users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    @staticmethod
    def get_user(user_id):
        """TODO: ADD PASSWORD CHECK BACK IN."""
        interface = DBInterface(db.session)
        try:
            user = interface.get_object(AuthUser, id=user_id)
            return user
        except NoResultFound:
            return False

    def get_user_with_credentials(self, password):
        interface = DBInterface(db.session)
        user = interface.get_object(AuthUser, email=self.email)
        if user:
            if check_password_hash(user.password, password):
                return user
            else:
                return False
        else:
            return "not found"

    def create_jwt_token(self):
        return create_access_token(self.email)

    @staticmethod
    def refresh_jwt_token(func):
        return create_access_token(identity=func())

    def add_user(self):
        """TODO: TEST OPERATIONAL FAILURE"""
        interface = DBInterface(db.session)
        num_retries = 5
        user_registration_success = False

        while num_retries > 0:
            try:
                interface.add_to_db(self)
                user_registration_success = True
                break
            except OperationalError:
                num_retries -= 1
                time.sleep(1)
            except IntegrityError:
                db.session.rollback()
                return False

        if not user_registration_success:
            return False
        return True
