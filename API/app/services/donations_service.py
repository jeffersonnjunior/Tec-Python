# API/app/services/donation_service.py
from sqlalchemy.orm import Session
from app.crud.donations_crud import create_donation, get_donation, update_donation, delete_donation
from app.schemas.donations_schema import DonationCreate, DonationUpdate

def create_donation_service(db: Session, donation: DonationCreate):
    return create_donation(db, donation)

def get_donation_service(db: Session, donation_id: int):
    return get_donation(db, donation_id)

def update_donation_service(db: Session, donation_id: int, donation: DonationUpdate):
    return update_donation(db, donation_id, donation)

def delete_donation_service(db: Session, donation_id: int):
    return delete_donation(db, donation_id)