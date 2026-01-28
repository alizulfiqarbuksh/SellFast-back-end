from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime
from .service import ServiceModel

class BookingModel(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    booking_datetime = Column(DateTime, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("UserModel", back_populates="bookings")

    service_id = Column(Integer, ForeignKey("services.id", ondelete="CASCADE"), nullable=False)
    service = relationship("ServiceModel", back_populates="bookings")
