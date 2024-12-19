from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import OrphanageBase
from app.schemas.orphanages_schema import Orphanage, OrphanageCreate, OrphanageUpdate
from app.services.orphanages_service import create_orphanage_service, get_orphanage_service, update_orphanage_service, delete_orphanage_service
from app.exceptions import InvalidCepError, OrphanageAlreadyExistsError

router = APIRouter(prefix="/orphanages", tags=["orphanages"])

@router.post("/", response_model=OrphanageBase)
def create(orphanage: OrphanageCreate, db: Session = Depends(get_db)):
    try:
        return create_orphanage_service(db, orphanage)
    except InvalidCepError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except OrphanageAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e))
@router.get("/{orphanage_id}", response_model=Orphanage)
def read(orphanage_id: int, db: Session = Depends(get_db)):
    db_orphanage = get_orphanage_service(db, orphanage_id)
    if db_orphanage is None:
        raise HTTPException(status_code=404, detail="Orphanage not found")
    return db_orphanage

@router.put("/{orphanage_id}", response_model=OrphanageBase)
def update(orphanage_id: int, orphanage: OrphanageUpdate, db: Session = Depends(get_db)):
    try:
        db_orphanage = update_orphanage_service(db, orphanage_id, orphanage)
        if db_orphanage is None:
            raise HTTPException(status_code=404, detail="Orphanage not found")
        return db_orphanage
    except InvalidCepError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except OrphanageAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.delete("/{orphanage_id}", response_model=Orphanage)
def delete(orphanage_id: int, db: Session = Depends(get_db)):
    db_orphanage = delete_orphanage_service(db, orphanage_id)
    if db_orphanage is None:
        raise HTTPException(status_code=404, detail="Orphanage not found")
    return db_orphanage