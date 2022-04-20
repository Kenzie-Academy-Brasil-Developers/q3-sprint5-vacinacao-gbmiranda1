from flask import Flask
from app.routes.vaccine_route import bp_vaccine

def init_app(app):
    app.register_blueprint(bp_vaccine)