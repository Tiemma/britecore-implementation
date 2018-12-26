"""
Model class for the user
"""
from typing import Dict, AnyStr, Type

from flask_jwt_extended import create_refresh_token, create_access_token
from passlib.hash import pbkdf2_sha256 as sha256

from src.model import DbModel, db


class Users(DbModel):
    """
    Model class implementation
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # Leaving this a string as a UUID / hash of the username would be easy to manage
    iws_employee_id = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    password = None

    def __repr__(self):
        return '<{} {}>'.format(self.__table__, self.__dict__)

    @property
    def password(self):
        raise Exception("You cannot view this property")

    @password.setter
    def password(self, password: AnyStr):
        """

        :param password:
        :return:
        """
        self.password_hash = sha256.hash(password)

    def verify_password(self, password: AnyStr) -> bool:
        """

        :param password:
        :return:
        """
        return sha256.verify(password, self.password_hash)

    @staticmethod
    def create_jwt_tokens(data: Type[DbModel]) -> Dict:
        return {"access_token": create_access_token(data), "refresh_token": create_refresh_token(data)}


if __name__ == "__main__":
    payload = {'iws_employee_id': 'string', 'username': 'string', 'email': 'emmanueltimmy98@gmail.com', 'password': 'string'}
    print(Users(**payload))


