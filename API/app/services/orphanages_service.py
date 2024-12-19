from sqlalchemy.orm import Session
from app.crud.orphanages_crud import create_orphanage, get_orphanage, update_orphanage, delete_orphanage
from app.schemas import OrphanageBase
from app.schemas.orphanages_schema import OrphanageCreate, OrphanageUpdate
from app.clients.viacep_client import get_address_by_cep

def create_orphanage_service(db: Session, orphanage: OrphanageCreate):
    address_data = get_address_by_cep(orphanage.cep)
    orphanage_data = orphanage.dict()
    orphanage_data["state"] = address_data.get("uf", "")
    orphanage_data["city"] = address_data.get("localidade", "")
    orphanage_base = OrphanageBase(**orphanage_data)
    return create_orphanage(db, orphanage_base)

def get_orphanage_service(db: Session, orphanage_id: int):
    return get_orphanage(db, orphanage_id)

def update_orphanage_service(db: Session, orphanage_id: int, orphanage: OrphanageUpdate):
    address_data = get_address_by_cep(orphanage.cep)
    orphanage_data = orphanage.dict()
    orphanage_data["state"] = address_data.get("uf", "")
    orphanage_data["city"] = address_data.get("localidade", "")
    return update_orphanage(db, orphanage_id, OrphanageBase(**orphanage_data))

def delete_orphanage_service(db: Session, orphanage_id: int):
    return delete_orphanage(db, orphanage_id)