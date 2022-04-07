from http import HTTPStatus
from flask import request, jsonify, current_app
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError


from app.models.vacina_model import Vacina
from . import verify_keys


def criar_vacina():
    data = request.get_json()

    try:
        verify_keys(data)
    except (KeyError, TypeError) as err:
        return err.args[0], HTTPStatus.BAD_REQUEST

    new_data = {
        "cpf": data['cpf'],
        "name": data['name'].lower(),
        "vaccine_name": data['vaccine_name'].lower(),
        "health_unit_name": data['health_unit_name'].lower()
    }

    vacina = Vacina(**new_data)

    try:
        current_app.db.session.add(vacina)
        current_app.db.session.commit()
    except (UniqueViolation, IntegrityError):
        return {"error": 'This CPF already exists in database'}, HTTPStatus.CONFLICT

    vacina_serialized = {
        "cpf": vacina.cpf,
        "name": vacina.name,
        "first_shot_date": vacina.first_shot_date,
        "second_shot_date": vacina.second_shot_date,
        "vaccine_name": vacina.vaccine_name,
        "health_unit_name": vacina.health_unit_name
    }

    return jsonify(vacina_serialized), HTTPStatus.CREATED

def listar_vacinas():

    vacinas = (
        Vacina.query.all()
    )

    serializer = [
        {
            "cpf": vacina.cpf,
            "name": vacina.name,
            "first_shot_date": vacina.first_shot_date,
            "second_shot_date": vacina.second_shot_date,
            "vaccine_name": vacina.vaccine_name,
            "health_unit_name": vacina.health_unit_name
        } for vacina in list(vacinas)
    ]

    return jsonify(serializer), HTTPStatus.OK