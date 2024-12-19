from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_config import Base

class Associate(Base):
    __tablename__ = "associates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    document = Column(String, unique=True, nullable=False)

    donations = relationship("Donation", back_populates="associate")