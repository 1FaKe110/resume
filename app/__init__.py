# app/__init__.py
from flask import Flask
from config import Config
from models import db
import os

app = Flask(__name__)


def create_app():
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
