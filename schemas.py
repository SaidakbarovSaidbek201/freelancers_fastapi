from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    available = "available"
    busy = "busy"
    on_leave = "on_leave"


class FreelancerBase(BaseModel):
    full_name: str
    phone_number: str
    skills: List[str]
    status: StatusEnum  

    @validator("phone_number")
    def validate_phone_number(cls, v):
        if not v.startswith("+998"):
            raise ValueError("Telefon raqami +998 bilan boshlanishi kerak.")
        return v

    @validator("skills")
    def validate_skills(cls, v):
        if not v or len(v) == 0:
            raise ValueError("Kamida 1 ta skill bo'lishi kerak.")
        return v


class FreelancerCreate(FreelancerBase):
    pass


class FreelancerUpdate(FreelancerBase):
    pass


class Freelancer(FreelancerBase):
    id: int
    joined_at: datetime 

    class Config:
        orm_mode = True
