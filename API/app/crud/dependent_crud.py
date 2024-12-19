from sqlalchemy.orm import Session
from app.database.models.dependent_model import Dependent
from app.schemas.dependent_schema import DependentCreate, DependentUpdate
from sqlalchemy.exc import IntegrityError
from app.exceptions import DocumentNotUniqueError

def create_dependent(db: Session, dependent: DependentCreate):
    db_dependent = Dependent(**dependent.dict())
    try:
        db.add(db_dependent)
        db.commit()
        db.refresh(db_dependent)
    except IntegrityError as e:
        db.rollback()
        if "document" in str(e.orig):
            raise DocumentNotUniqueError(dependent.document)
    return db_dependent


def get_dependent(db: Session, dependent_id: int):
    return db.query(Dependent).filter(Dependent.id == dependent_id).first()


def update_dependent(db: Session, dependent_id: int, dependent: DependentUpdate):
    db_dependent = db.query(Dependent).filter(Dependent.id == dependent_id).first()
    if not db_dependent:
        raise ValueError("Dependente não existe")

    for key, value in dependent.dict().items():
        setattr(db_dependent, key, value)
    try:
        db.commit()
        db.refresh(db_dependent)
    except IntegrityError as e:
        db.rollback()
        if "document" in str(e.orig):
            raise DocumentNotUniqueError(dependent.document)
    return db_dependent

def delete_dependent(db: Session, dependent_id: int):
    db_dependent = db.query(Dependent).filter(Dependent.id == dependent_id).first()
    if db_dependent:
        db.delete(db_dependent)
        db.commit()
    return db_dependent