"""
Factory for initializing all flask app extensions
"""
from os import getenv

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.config import CONFIG_BY_NAME

app = Flask(__name__)
app.config.from_object(CONFIG_BY_NAME[getenv('ENVIRONMENT', 'development')])

db = SQLAlchemy(app)

# Models imported after creating db instance
from src.model import Client, FeatureRequest, ProductArea, User

migrate = Migrate(app, db)
