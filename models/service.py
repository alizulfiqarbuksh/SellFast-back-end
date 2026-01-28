from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import relationship
from .base import Base

class ServiceModel(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)  
    image = Column(String, nullable=True)

    # Relationships
    bookings = relationship("BookingModel", back_populates="service", cascade="all, delete")
