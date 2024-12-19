from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_config import Base

class Orphanage(Base):
    __tablename__ = "orphanages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, nullable=False)
    contact_number = Column(String, nullable=True)
    registration_date = Column(DateTime, default=datetime.utcnow)
    cep = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)

    donations = relationship("Donation", back_populates="orphanage")
    dependents = relationship("Dependent", back_populates="orphanage")


