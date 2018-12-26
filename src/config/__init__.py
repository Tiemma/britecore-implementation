"""
Project level flask configuration

"""

from os import urandom, getenv
from os.path import join, abspath


class Config:
    """
    Config base class
    """

    # Flask native configs
    DEBUG = True
    SECRET_KEY = urandom(256)
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = urandom(256)
    THREADS_PER_PAGE = 1

    # Flask restplus configs
    RESTPLUS_VALIDATE = True

    # JWT configs
    JWT_SECRET_KEY = urandom(256)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_ERROR_MESSAGE_KEY = "message"

    # SQL Alchemy configs
    SQLALCHEMY_DATABASE_URI = "sqlite:///{db}".format(db=abspath(join(getenv('DB_LOCATION', '../database'), 'app.db')))
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    def __repr__(self):
        return '<Config {}>'.format(Config.__dict__)


class Development(Config):
    """
    Development configuration
    """
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "sqlite:///{db}".format(db=abspath(join(getenv('DB_LOCATION', '/tmp'), 'app.db')))

    def __repr__(self):
        return '<Development {}>'.format(Development.__dict__)


class Testing(Config):
    """
    Testing configuration
    """
    FLASK_ENV='testing'

    def __repr__(self):
        return '<Testing {}>'.format(Testing.__dict__)


class Production(Config):
    """
    Production configuration
    """
    DEBUG = False
    FLASK_ENV='production'
    THREADS_PER_PAGE = 8
    SQLALCHEMY_ECHO = False
    QUERYINSPECT_ENABLED = False

    def __repr__(self):
        return '<Production {}>'.format(Production.__dict__)


CONFIG_BY_NAME = dict(
    development=Development,
    production=Production,
    testing=Testing
)

if __name__ == "__main__":
    print(Config())
