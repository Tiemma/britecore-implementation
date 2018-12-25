"""
Project level flask configuration

"""

from os import urandom, getenv

DEFAULT_POSTGRES_USER = "postgres"
DEFAULT_POSTGRES_PASSWORD = "password"
DEFAULT_POSTGRES_DB = "stackoverflow"
DEFAULT_POSTGRES_HOST = "localhost"
DEFAULT_POSTGRES_PORT = 5432


class Config:
    """
    Config base class
    """
    DEBUG = True
    SECRET_KEY = urandom(256)
    POSTGRES_CONFIG = {
        'user': getenv('POSTGRES_USER', DEFAULT_POSTGRES_USER),
        'password': getenv('POSTGRES_PASSWORD', DEFAULT_POSTGRES_PASSWORD),
        'dbname': getenv('POSTGRES_DB', DEFAULT_POSTGRES_DB),
        'host': getenv('POSTGRES_HOST', DEFAULT_POSTGRES_HOST),
        'port': getenv('POSTGRES_PORT', DEFAULT_POSTGRES_PORT),
    }
    DATABASE_URI = """postgresql://
    %(user)s:%(password)s@
    %(host)s:%(port)s/%(dbname)s""" % POSTGRES_CONFIG
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
    print(Config)
