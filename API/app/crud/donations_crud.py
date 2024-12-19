# API/app/crud/donation_crud.py
from sqlalchemy.orm import Session
from app.database.models.donations_model import Donation
from app.database.models.associate_model import Associate
from app.database.models.orphanages_model import Orphanage
from app.database.models.donations_model import Donation
from app.schemas.donations_schema import DonationCreate, DonationUpdate
from app.exceptions import RecordNotFoundError

def create_donation(db: Session, donation: DonationCreate):
    if not db.query(Associate).filter(Associate.id == donation.associate_id).first():
        raise RecordNotFoundError("Associado", donation.associate_id)

    elif not db.query(Orphanage).filter(Orphanage.id == donation.orphanage_id).first():
        raise RecordNotFoundError("Orfanato", donation.orphanage_id)

    db_donation = Donation(**donation.dict())
    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)
    return db_donation

def get_donation(db: Session, donation_id: int):
    return db.query(Donation).filter(Donation.id == donation_id).first()

def update_donation(db: Session, donation_id: int, donation: DonationUpdate):
    if not db.query(Associate).filter(Associate.id == donation.associate_id).first():
        raise RecordNotFoundError("Associado", donation.associate_id)

    elif not db.query(Orphanage).filter(Orphanage.id == donation.orphanage_id).first():
        raise RecordNotFoundError("Orfanato", donation.orphanage_id)

    db_donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if db_donation:
        for key, value in donation.dict().items():
            setattr(db_donation, key, value)
        db.commit()
        db.refresh(db_donation)
    return db_donation

def delete_donation(db: Session, donation_id: int):
    db_donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if db_donation:
        db.delete(db_donation)
        db.commit()
    return db_donation