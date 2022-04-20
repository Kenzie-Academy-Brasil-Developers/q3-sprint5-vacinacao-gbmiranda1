from flask import Flask
from flask_migrate import Migrate


def init_app(app):

    from app.models.vaccine_model import VaccineModel

    Migrate(app, app.db)
