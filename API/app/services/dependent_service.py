from sqlalchemy.orm import Session
from app.crud.dependent_crud import create_dependent, get_dependent, update_dependent, delete_dependent
from app.schemas.dependent_schema import DependentCreate, DependentUpdate

def create_dependent_service(db: Session, dependent: DependentCreate):
    return create_dependent(db, dependent)

def get_dependent_service(db: Session, dependent_id: int):
    return get_dependent(db, dependent_id)

def update_dependent_service(db: Session, dependent_id: int, dependent: DependentUpdate):
    return update_dependent(db, dependent_id, dependent)

def delete_dependent_service(db: Session, dependent_id: int):
    return delete_dependent(db, dependent_id)