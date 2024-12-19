from sqlalchemy.orm import Session
from app.database.models import Associate
from app.schemas import AssociateBase
from sqlalchemy.exc import IntegrityError
from app.exceptions import DocumentNotUniqueError


def create_associate(db: Session, associate: AssociateBase):
    db_associate = Associate(**associate.dict())
    try:
        db.add(db_associate)
        db.commit()
        db.refresh(db_associate)
    except IntegrityError as e:
        db.rollback()
        if "document" in str(e.orig):
            raise DocumentNotUniqueError(associate.document)
    return db_associate


def get_associate(db: Session, associate_id: int):
    return db.query(Associate).filter(Associate.id == associate_id).first()


def update_associate(db: Session, associate_id: int, associate: AssociateBase):
    db_associate = db.query(Associate).filter(Associate.id == associate_id).first()
    if not db_associate:
        raise ValueError("Associado não existe")

    for key, value in associate.dict().items():
        setattr(db_associate, key, value)
    try:
        db.commit()
        db.refresh(db_associate)
    except IntegrityError as e:
        db.rollback()
        if "document" in str(e.orig):
            raise DocumentNotUniqueError(associate.document)
    return db_associate


def delete_associate(db: Session, associate_id: int):
    db_associate = db.query(Associate).filter(Associate.id == associate_id).first()
    if db_associate:
        db.delete(db_associate)
        db.commit()
    return db_associate