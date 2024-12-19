from pydantic import BaseModel, Field
from datetime import datetime

class OrphanageBase(BaseModel):
    name: str
    address: str
    contact_number: str | None = None
    cep: str
    state: str
    city: str


class OrphanageCreate(BaseModel):
    name: str
    address: str
    contact_number: str | None = None
    cep: str

class OrphanageUpdate(BaseModel):
    name: str
    address: str
    contact_number: str | None = None
    cep: str

class Orphanage(OrphanageBase):
    id: int
    registration_date: datetime

    class Config:
        orm_mode = True

