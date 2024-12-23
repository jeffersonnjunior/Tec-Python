import pytest
from sqlalchemy.orm import Session
from app.crud.donations_crud import (
    create_donation,
    get_donation,
    update_donation,
    delete_donation
)
from app.schemas.donations_schema import DonationCreate, DonationUpdate
from app.database.models.associate_model import Associate
from app.database.models.orphanages_model import Orphanage
from app.exceptions import RecordNotFoundError

def test_create_donation(db: Session):
    associate = Associate(name="Associate 1", document="123456789", email="associate1@example.com")
    db.add(associate)
    db.commit()
    db.refresh(associate)

    orphanage = Orphanage(name="Orphanage 1", address="Address 1", contact_number="123456789", cep="12345678", state="State 1", city="City 1")
    db.add(orphanage)
    db.commit()
    db.refresh(orphanage)

    donation = DonationCreate(
        amount=100.0,
        associate_id=associate.id,
        orphanage_id=orphanage.id
    )
    result = create_donation(db, donation)
    assert result.amount == donation.amount
    assert result.associate_id == donation.associate_id
    assert result.orphanage_id == donation.orphanage_id

def test_get_donation(db: Session):
    associate = Associate(name="Associate 1", document="123456789", email="associate1@example.com")
    db.add(associate)
    db.commit()
    db.refresh(associate)

    orphanage = Orphanage(name="Orphanage 1", address="Address 1", contact_number="123456789", cep="12345678", state="State 1", city="City 1")
    db.add(orphanage)
    db.commit()
    db.refresh(orphanage)

    donation = DonationCreate(
        amount=100.0,
        associate_id=associate.id,
        orphanage_id=orphanage.id
    )
    created_donation = create_donation(db, donation)
    donation_id = created_donation.id

    result = get_donation(db, donation_id)
    assert result.id == donation_id

def test_update_donation(db: Session):
    associate = Associate(name="Associate 1", document="123456789", email="associate1@example.com")
    db.add(associate)
    db.commit()
    db.refresh(associate)

    orphanage = Orphanage(name="Orphanage 1", address="Address 1", contact_number="123456789", cep="12345678", state="State 1", city="City 1")
    db.add(orphanage)
    db.commit()
    db.refresh(orphanage)

    donation = DonationCreate(
        amount=100.0,
        associate_id=associate.id,
        orphanage_id=orphanage.id
    )
    created_donation = create_donation(db, donation)
    donation_id = created_donation.id

    updated_donation = DonationUpdate(
        amount=200.0,
        associate_id=associate.id,
        orphanage_id=orphanage.id
    )
    result = update_donation(db, donation_id, updated_donation)
    assert result.amount == updated_donation.amount

def test_delete_donation(db: Session):
    associate = Associate(name="Associate 1", document="123456789", email="associate1@example.com")
    db.add(associate)
    db.commit()
    db.refresh(associate)

    orphanage = Orphanage(name="Orphanage 1", address="Address 1", contact_number="123456789", cep="12345678", state="State 1", city="City 1")
    db.add(orphanage)
    db.commit()
    db.refresh(orphanage)

    donation = DonationCreate(
        amount=100.0,
        associate_id=associate.id,
        orphanage_id=orphanage.id
    )
    created_donation = create_donation(db, donation)
    donation_id = created_donation.id

    result = delete_donation(db, donation_id)
    assert result.id == donation_id