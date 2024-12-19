from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import AssociateBase
from app.services import create_associate_service, get_associate_service, update_associate_service, delete_associate_service
from app.exceptions import DocumentNotUniqueError

router = APIRouter(prefix="/associate", tags=["associate"])

@router.post("/", response_model=AssociateBase)
def create(associate: AssociateBase, db: Session = Depends(get_db)):
    try:
        return create_associate_service(db, associate)
    except DocumentNotUniqueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{associate_id}", response_model=AssociateBase)
def read(associate_id: int, db: Session = Depends(get_db)):
    db_associate = get_associate_service(db, associate_id)
    if db_associate is None:
        raise HTTPException(status_code=404, detail="Associado não existe")
    return db_associate

@router.put("/{associate_id}", response_model=AssociateBase)
def update(associate_id: int, associate: AssociateBase, db: Session = Depends(get_db)):
    try:
        db_associate = update_associate_service(db, associate_id, associate)
        return db_associate
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DocumentNotUniqueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{associate_id}", response_model=AssociateBase)
def delete(associate_id: int, db: Session = Depends(get_db)):
    db_associate = delete_associate_service(db, associate_id)
    if db_associate is None:
        raise HTTPException(status_code=404, detail="Associado não existe")
    return db_associate