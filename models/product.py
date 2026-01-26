from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from .base import Base

from .review import ReviewModel

class ProductModel(Base):
    
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)

    # Relationships
    # cart_items = relationship("CartItemModel", back_populates="product")
    order_items = relationship("OrderItemModel", back_populates="product")
    
    reviews = relationship( "ReviewModel",back_populates="product",cascade="all, delete-orphan",passive_deletes=True)

