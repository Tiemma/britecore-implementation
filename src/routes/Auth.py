"""
AUTH_NS definitions for authentication [Login / Signup]
"""

from flask import request
from flask_restplus import Resource, fields, Namespace
from flask_restplus._http import HTTPStatus

from src.controller import ResponseBody
from src.logger import Logger
from src.model import db
from src.model.Users import Users

AUTH_NS = Namespace("auth", description="Authentication related operations")

LOGIN = AUTH_NS.model('Auth', {
    'username': fields.String(required=True, description='The users pet name'),
    'password': fields.String(required=True, description='User password sent on signup and login')
})

REGISTER = AUTH_NS.model('User', {
    'iws_employee_id': fields.String(required=True, description='The employee id of the user with access to this '
                                                                'dashboard'),
    'username': fields.String(required=True, description='The users pet name'),
    'email': fields.String(required=True, description='The users email'),
    'password': fields.String(required=True, description='User password sent on signup and login')
})


@AUTH_NS.route("/login")
@AUTH_NS.response(HTTPStatus.NOT_FOUND,
                  "User not found and authentication request rejected")
class Login(Resource):
    """
    Login controller resource
    """
    logger = Logger.get_logger(__name__)

    @AUTH_NS.expect(LOGIN)
    def post(self):
        """

        :return:
        """
        payload = request.json
        self.logger.debug(payload)
        return {}, HTTPStatus.OK


@AUTH_NS.route("/logout")
@AUTH_NS.response(HTTPStatus.NOT_FOUND,
                  "User not found and logout request rejected")
class Logout(Resource):
    """
    Login controller resource
    """
    logger = Logger.get_logger(__name__)

    @AUTH_NS.expect(LOGIN)
    def post(self):
        """

        :return:
        """
        payload = AUTH_NS.payload
        self.logger.debug(payload)
        return {}, HTTPStatus.OK


@AUTH_NS.route("/register")
@AUTH_NS.response(HTTPStatus.NOT_FOUND,
                  "Server down while processing registration")
@AUTH_NS.response(HTTPStatus.CONFLICT,
                  "User details are already existent")
@AUTH_NS.response(HTTPStatus.CREATED,
                  "User details have been successfully registered in the database")
class Register(Resource):
    """
    Login controller resource
    """
    logger = Logger.get_logger(__name__)

    @AUTH_NS.expect(REGISTER, validate=True)
    def post(self):
        """

        :return:
        """
        payload = request.json
        self.logger.debug("Payload variables: %r", payload)
        try:
            data = Users(**payload)
            token = Users.create_jwt_tokens(data.as_dict())
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            print(e)
            return {'An error occurred'}, 500
        else:
            return ResponseBody(data.as_dict(), "User was registered successfully", HTTPStatus.CREATED, token=token).body

