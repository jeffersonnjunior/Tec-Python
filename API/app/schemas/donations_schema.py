from pydantic import BaseModel
from datetime import datetime

class DonationBase(BaseModel):
    amount: float
    associate_id: int
    orphanage_id: int

class DonationCreate(DonationBase):
    pass

class DonationUpdate(DonationBase):
    pass

class Donation(DonationBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True