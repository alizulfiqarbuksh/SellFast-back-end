from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .product import ProductModel

class OrderItemModel(Base):

    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    # Relationships (use string names - SQLAlchemy resolves them at runtime)
    order = relationship("OrderModel", back_populates="items")
    product = relationship("ProductModel", back_populates="order_items")
