import pytest
from sqlalchemy.orm import Session
from app.crud.orphanages_crud import (
    create_orphanage,
    get_orphanage,
    update_orphanage,
    delete_orphanage
)
from app.schemas.orphanages_schema import OrphanageBase
from app.exceptions import OrphanageAlreadyExistsError

def test_create_orphanage(db: Session):
    orphanage = OrphanageBase(
        name="Orphanage 1",
        address="Address 1",
        contact_number="123456789",
        cep="12345678",
        state="State 1",
        city="City 1"
    )
    result = create_orphanage(db, orphanage)
    assert result.name == orphanage.name

def test_get_orphanage(db: Session):
    orphanage_id = 1
    result = get_orphanage(db, orphanage_id)
    assert result.id == orphanage_id

def test_update_orphanage(db: Session):
    orphanage_id = 1
    orphanage = OrphanageBase(
        name="Updated Orphanage",
        address="Updated Address",
        contact_number="987654321",
        cep="87654321",
        state="Updated State",
        city="Updated City"
    )
    result = update_orphanage(db, orphanage_id, orphanage)
    assert result.name == orphanage.name

def test_delete_orphanage(db: Session):
    orphanage_id = 1
    result = delete_orphanage(db, orphanage_id)
    assert result.id == orphanage_id