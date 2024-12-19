from sqlalchemy import Column, Float, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_config import Base

class Dependent(Base):
    __tablename__ = "dependents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(Date, nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String, nullable=True)
    orphanage_id = Column(Integer, ForeignKey('orphanages.id'))
    document = Column(String, unique=True, nullable=False)

    orphanage = relationship("Orphanage", back_populates="dependents")