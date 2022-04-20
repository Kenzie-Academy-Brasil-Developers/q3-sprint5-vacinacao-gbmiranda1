from flask import Blueprint
from app.controllers.vaccine_controller import create_vaccine, get_vaccine

bp_vaccine= Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")

bp_vaccine.post("")(create_vaccine)
bp_vaccine.get("")(get_vaccine)