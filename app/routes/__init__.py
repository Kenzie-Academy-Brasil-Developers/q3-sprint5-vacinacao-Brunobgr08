from flask import Blueprint, Flask
from app.routes.vacina_route import bp as bp_vacina


bp_api = Blueprint("api", __name__, url_prefix="")


def init_app(app: Flask):

    bp_api.register_blueprint(bp_vacina)

    app.register_blueprint(bp_api)