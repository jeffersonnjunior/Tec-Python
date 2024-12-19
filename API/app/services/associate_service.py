from sqlalchemy.orm import Session
from app.crud import get_associate, create_associate, update_associate, delete_associate
from app.schemas import AssociateBase

def create_associate_service(db: Session, associate: AssociateBase):
    return create_associate(db, associate)

def get_associate_service(db: Session, associate_id: int):
    return get_associate(db, associate_id)

def update_associate_service(db: Session, associate_id: int, associate: AssociateBase):
    return update_associate(db, associate_id, associate)

def delete_associate_service(db: Session, associate_id: int):
    return delete_associate(db, associate_id)