from datetime import datetime, timedelta
from sqlalchemy import Column, String, DateTime
from dataclasses import dataclass
from app.configs.database import db

@dataclass
class VaccineModel(db.Model):
    __tablename__ = "vaccine_cards"
    date = datetime.now()

    name = Column(String, nullable=False)
    cpf = Column(String(11), primary_key=True)
    first_shot_date = Column(DateTime, default=date)
    second_shot_date = Column(DateTime, default=date + timedelta(days=90))
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String, nullable=False)
