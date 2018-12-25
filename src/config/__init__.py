"""
Project level flask configuration

"""

from os import urandom, getenv
from os.path import join, abspath



class Config:
    """
    Config base class
    """
    DEBUG = True
    SECRET_KEY = urandom(256)
    SQLALCHEMY_DATABASE_URI = "sqlite:///{db}".format(db=abspath(join('../../database', 'app.db')))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = urandom(256)
    RESTPLUS_VALIDATE = True
    JWT_SECRET_KEY = urandom(256)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_ERROR_MESSAGE_KEY = "message"


class Development(Config):
    """
    Development configuration
    """
    THREADS_PER_PAGE = 1


class Testing(Config):
    """
    Development configuration
    """
    THREADS_PER_PAGE = 1


class Production(Config):
    """
    Production configuration
    """
    DEBUG = False
    THREADS_PER_PAGE = 8


CONFIG_BY_NAME = dict(
    development=Development,
    production=Production,
    testing=Testing
)

if __name__ == "__main__":
    print(Config.__dict__)
