from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_config import Base

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    associate_id = Column(Integer, ForeignKey('associates.id'))
    orphanage_id = Column(Integer, ForeignKey('orphanages.id'))

    associate = relationship("Associate", back_populates="donations")
    orphanage = relationship("Orphanage", back_populates="donations")
