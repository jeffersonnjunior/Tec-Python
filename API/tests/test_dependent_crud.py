import pytest
from sqlalchemy.orm import Session
from app.crud.associate_crud import (
    create_associate,
    get_associate,
    update_associate,
    delete_associate
)
from app.schemas import AssociateBase
from app.exceptions import DocumentNotUniqueError

def test_create_associate(db: Session):
    associate = AssociateBase(
        name="Associate 1",
        document="123456789",
        email="associate1@example.com"
    )
    result = create_associate(db, associate)
    assert result.name == associate.name
    assert result.document == associate.document
    assert result.email == associate.email

def test_get_associate(db: Session):
    associate = AssociateBase(
        name="Associate 1",
        document="123456789",
        email="associate1@example.com"
    )
    created_associate = create_associate(db, associate)
    associate_id = created_associate.id

    result = get_associate(db, associate_id)
    assert result.id == associate_id

def test_update_associate(db: Session):
    associate = AssociateBase(
        name="Associate 1",
        document="123456789",
        email="associate1@example.com"
    )
    created_associate = create_associate(db, associate)
    associate_id = created_associate.id

    updated_associate = AssociateBase(
        name="Updated Associate",
        document="987654321",
        email="updated@example.com"
    )
    result = update_associate(db, associate_id, updated_associate)
    assert result.name == updated_associate.name
    assert result.document == updated_associate.document
    assert result.email == updated_associate.email

def test_delete_associate(db: Session):
    associate = AssociateBase(
        name="Associate 1",
        document="123456789",
        email="associate1@example.com"
    )
    created_associate = create_associate(db, associate)
    associate_id = created_associate.id

    result = delete_associate(db, associate_id)
    assert result.id == associate_id