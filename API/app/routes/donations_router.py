from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.donations_schema import Donation, DonationCreate, DonationUpdate
from app.services.donations_service import create_donation_service, get_donation_service, update_donation_service, delete_donation_service
from app.exceptions import RecordNotFoundError

router = APIRouter(prefix="/donations", tags=["donations"])

@router.post("/", response_model=Donation)
def create(donation: DonationCreate, db: Session = Depends(get_db)):
    try:
        return create_donation_service(db, donation)
    except RecordNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
@router.get("/{donation_id}", response_model=Donation)
def read(donation_id: int, db: Session = Depends(get_db)):
    db_donation = get_donation_service(db, donation_id)
    if db_donation is None:
        raise HTTPException(status_code=404, detail="Doação não registrada")
    return db_donation

@router.put("/{donation_id}", response_model=Donation)
def update(donation_id: int, donation: DonationUpdate, db: Session = Depends(get_db)):
    try:
        return update_donation_service(db, donation_id, donation)
    except RecordNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{donation_id}", response_model=Donation)
def delete(donation_id: int, db: Session = Depends(get_db)):
    db_donation = delete_donation_service(db, donation_id)
    if db_donation is None:
        raise HTTPException(status_code=404, detail="Doação não registrada")
    return db_donation