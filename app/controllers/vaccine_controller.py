from http import HTTPStatus
from logging.config import valid_ident
from app.models.vaccine_model import VaccineModel
from sqlalchemy.exc import IntegrityError
from app.configs.database import db
from flask import request, jsonify

request_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]

def create_vaccine():
    request_data = request.get_json()
    data = {"cpf": request_data["cpf"], "name": request_data["name"], "vaccine_name": request_data["vaccine_name"], "health_unit_name": request_data["health_unit_name"]}
    data_keys = data.keys()
    missing_keys = []
    missing_values_type = []

    for values in data.values():
        if type(values) is not str:
            missing_values_type.append(values)
    if len(missing_values_type) > 0:
        return {"error": "request must be in string"}, HTTPStatus.BAD_REQUEST


    for key in request_keys:
        if key not in data_keys:
            missing_keys.append(key)
    if len(missing_keys) > 0:
        return {"error": f"missing key {missing_keys}"}, HTTPStatus.BAD_REQUEST


    try:
        if len(data["cpf"]) != 11:
            return {"error": "cpf must contain 11 characters"}, 400
        else:

            data["health_unit_name"] = data["health_unit_name"].title()
            data["name"] = data["name"].title()
            vaccine = VaccineModel(**data)
            db.session.add(vaccine)
            db.session.commit()
          
            return jsonify({
                "name": vaccine.name,
                "cpf": vaccine.cpf,
                "vaccine_name": vaccine.vaccine_name,
                "health_unit_name": vaccine.health_unit_name,
                "first_shot_date": vaccine.first_shot_date,
                "second_shot_date": vaccine.second_shot_date,
            }), HTTPStatus.CREATED
    except IntegrityError:
        return jsonify({"error": "cpf already registered"}), HTTPStatus.CONFLICT
    except (TypeError):
        return jsonify({"error": {"expected_keys": request_keys,"incoming_keys": missing_keys}}), HTTPStatus.BAD_REQUEST


def get_vaccine():
    vaccines = (
        VaccineModel
        .query
        .all()
    )
    result = []
    for vaccine in vaccines:
        vaccine = vaccine.__dict__
        vaccine.pop('_sa_instance_state', None)
        result.append(vaccine)
    return jsonify({"vaccines_card": result}), HTTPStatus.OK