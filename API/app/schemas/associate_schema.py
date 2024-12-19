from pydantic import BaseModel, Field

class AssociateBase(BaseModel):
    name: str
    email: str
    document: str = Field(..., unique=True)

class AssociateCreate(AssociateBase):
    pass

class AssociateUpdate(AssociateBase):
    pass

class Associate(AssociateBase):
    id: int

    class Config:
        orm_mode: True