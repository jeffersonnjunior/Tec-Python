from fastapi import APIRouter, Depends, HTTPException
from fastapi.exceptions import ResponseValidationError
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.dependent_schema import Dependent, DependentCreate, DependentUpdate
from app.services.dependent_service import create_dependent_service, get_dependent_service, update_dependent_service, delete_dependent_service
from app.exceptions import DocumentNotUniqueError

router = APIRouter(prefix="/dependents", tags=["dependents"])

@router.post("/", response_model=Dependent)
def create(dependent: DependentCreate, db: Session = Depends(get_db)):
    try:
        return create_dependent_service(db, dependent)
    except DocumentNotUniqueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{dependent_id}", response_model=Dependent)
def read(dependent_id: int, db: Session = Depends(get_db)):
    db_dependent = get_dependent_service(db, dependent_id)
    if db_dependent is None:
        raise HTTPException(status_code=404, detail="Dependente não existe")
    return db_dependent

@router.put("/{dependent_id}", response_model=Dependent)
def update(dependent_id: int, dependent: DependentUpdate, db: Session = Depends(get_db)):
    try:
        db_dependent = update_dependent_service(db, dependent_id, dependent)
        return db_dependent
    except DocumentNotUniqueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except (ResponseValidationError, Exception):
        raise HTTPException(status_code=404, detail="Dependente não existe")

@router.delete("/{dependent_id}", response_model=Dependent)
def delete(dependent_id: int, db: Session = Depends(get_db)):
    db_dependent = delete_dependent_service(db, dependent_id)
    if db_dependent is None:
        raise HTTPException(status_code=404, detail="Dependente não existe")
    return db_dependent