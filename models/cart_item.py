from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class CartItemModel(Base):
    
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False, default=1)

    # Relationships (use string names - SQLAlchemy resolves them at runtime)
    cart = relationship("CartModel", back_populates="items")
    product = relationship("ProductModel", back_populates="cart_items")
