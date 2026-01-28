from sqlalchemy import Column, Integer, Float, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

# from .user import UserModel

class ReviewModel(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Float, nullable=False)  
    comment = Column(Text, nullable=True)
    
    
    # Relationships
    product = relationship("ProductModel", back_populates="reviews")
    user = relationship("UserModel", back_populates="reviews")

    
    created_at = Column(DateTime, default=func.now())