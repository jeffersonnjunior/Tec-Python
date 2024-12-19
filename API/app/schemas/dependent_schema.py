from pydantic import BaseModel, Field
from datetime import date, datetime

class DependentBase(BaseModel):
    name: str
    birth_date: date
    notes: str | None = None
    orphanage_id: int
    document: str = Field(..., unique=True)

class DependentCreate(DependentBase):
    pass

class DependentUpdate(DependentBase):
    pass

class Dependent(DependentBase):
    id: int
    registration_date: datetime

    class Config:
        orm_mode = True