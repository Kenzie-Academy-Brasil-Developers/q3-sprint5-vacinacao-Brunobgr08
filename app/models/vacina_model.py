from app.configs.database import db
from sqlalchemy import Column, String, DateTime
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class Vacina(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime, default=datetime.now())
    second_shot_date = Column(DateTime, default=(datetime.now() + timedelta(90)))
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)
