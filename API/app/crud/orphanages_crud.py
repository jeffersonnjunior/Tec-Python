from sqlalchemy.orm import Session
from app.database.models.orphanages_model import Orphanage
from app.schemas.orphanages_schema import OrphanageBase
from app.exceptions import OrphanageAlreadyExistsError


def create_orphanage(db: Session, orphanage: OrphanageBase):
    existing_orphanage = db.query(Orphanage).filter(
        Orphanage.city == orphanage.city,
        Orphanage.contact_number == orphanage.contact_number,
        Orphanage.state == orphanage.state,
        Orphanage.cep == orphanage.cep,
    ).first()
    if existing_orphanage:
        raise OrphanageAlreadyExistsError(orphanage.address, orphanage.contact_number, orphanage.state, orphanage.cep)

    db_orphanage = Orphanage(**orphanage.dict())
    db.add(db_orphanage)
    db.commit()
    db.refresh(db_orphanage)
    return db_orphanage

def get_orphanage(db: Session, orphanage_id: int):
    return db.query(Orphanage).filter(Orphanage.id == orphanage_id).first()

def update_orphanage(db: Session, orphanage_id: int, orphanage: OrphanageBase):
    db_orphanage = db.query(Orphanage).filter(Orphanage.id == orphanage_id).first()
    if not db_orphanage:
        return None

    existing_orphanage = db.query(Orphanage).filter(
        Orphanage.city == orphanage.city,
        Orphanage.contact_number == orphanage.contact_number,
        Orphanage.state == orphanage.state,
        Orphanage.cep == orphanage.cep,
        Orphanage.id != orphanage_id
    ).first()
    if existing_orphanage:
        raise OrphanageAlreadyExistsError(orphanage.address, orphanage.contact_number, orphanage.state, orphanage.cep)

    for key, value in orphanage.dict().items():
        setattr(db_orphanage, key, value)
    db.commit()
    db.refresh(db_orphanage)
    return db_orphanage

def delete_orphanage(db: Session, orphanage_id: int):
    db_orphanage = db.query(Orphanage).filter(Orphanage.id == orphanage_id).first()
    if db_orphanage:
        db.delete(db_orphanage)
        db.commit()
    return db_orphanage