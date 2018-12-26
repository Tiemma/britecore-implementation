"""
Factory for initializing all flask app extensions
"""

from os import getenv, environ

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_queryinspect import QueryInspect

from src.config import CONFIG_BY_NAME
from src.logger import Logger
from src.routes import create_api
from src.model import db


class AppFactory:
    """
    App Factory for creating and managing flask app instances
    """
    __app = Flask(__name__)
    __api = None
    __db = db
    __jwt = None
    __migrate = None
    __query_inspect = None
    __limiter = None
    logger = Logger.get_logger(__name__)

    def __init__(self):
        config = CONFIG_BY_NAME[getenv('ENVIRONMENT', 'development')]
        environ['FLASK_ENV'] = config.FLASK_ENV
        self.logger.info("Database path: %s", config.SQLALCHEMY_DATABASE_URI)
        self.__app.config.from_object(config)

    def init_with_db(self):
        self.__db.init_app(self.__app)
        self.__migrate = Migrate(self.__app, self.__db)

    def init_with_api(self):
        self.__api = create_api().init_app(self.__app)
        self.__jwt = JWTManager(self.__app)
        self.__limiter = Limiter(
            self.__app,
            key_func=get_remote_address,
            default_limits=["60 per minute"],
        )
        for handler in self.__app.logger.handlers:
            self.__limiter.logger.addHandler(handler)
        CORS(self.__app)

    def init_with_query_inspect(self):
        self.__query_inspect = QueryInspect(self.__app)

    @property
    def api(self):
        return self.__api

    @property
    def app(self):
        return self.__app

    @property
    def db(self):
        return self.__db

    @property
    def api(self):
        return self.__api

    @property
    def jwt(self):
        return self.__jwt


