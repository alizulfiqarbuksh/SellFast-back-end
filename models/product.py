from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from .cart_item import CartItemModel

class ProductModel(Base):
    
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)
    image = Column(String, nullable=True)

    # Relationships
    cart_items = relationship("CartItemModel", back_populates="product")
    order_items = relationship("OrderItemModel", back_populates="product")
