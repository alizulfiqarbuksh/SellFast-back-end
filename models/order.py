from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class OrderModel(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships (use string names - SQLAlchemy resolves them at runtime)
    user = relationship("UserModel", back_populates="orders")
    items = relationship("OrderItemModel", back_populates="order", cascade="all, delete-orphan")
