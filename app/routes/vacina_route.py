from flask import Blueprint
from app.controllers import vacina_controller


bp = Blueprint("vacinas", __name__, url_prefix="/vaccinations")


bp.post("")(vacina_controller.criar_vacina)
bp.get("")(vacina_controller.listar_vacinas)
