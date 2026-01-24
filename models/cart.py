# from sqlalchemy import Column, Integer, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
# from .base import Base
# from models.user import UserModel

# class CartModel(Base):
    
#     __tablename__ = "carts"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), unique=True)
#     is_active = Column(Boolean, default=True)

#     # Relationships
#     user = relationship("UserModel", back_populates="cart")
#     items = relationship("CartItemModel", back_populates="cart", cascade="all, delete-orphan")
