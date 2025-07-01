from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import JSON
from database import Base
from datetime import datetime

class Freelancer(Base):
    __tablename__ = 'freelancers'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    skills = Column(JSON, nullable=False)
    status = Column(String, nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow, nullable=False)
