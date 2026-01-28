from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class ReviewSchema(BaseModel):
    id: int
    username: str
    rating: float
    comment: Optional[str] = None
    user_id: int
    product_id: int
    created_at: datetime 

    class Config:
        orm_mode = True

class CreateReviewSchema(BaseModel):
    rating: float = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=1000)
    
    @field_validator('rating')
    @classmethod
    def validate_rating(cls, v):
        
        if v % 0.5 != 0:
            raise ValueError('Rating must be in 0.5 increments (1, 1.5, 2, 2.5, etc.)')
        return v
    
    class Config:
        orm_mode = True

class UpdateReviewSchema(BaseModel):
    rating: Optional[float] = Field(None, ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=1000)
    
    @field_validator('rating')
    @classmethod
    def validate_rating(cls, v):
        if v is not None and v % 0.5 != 0:
            raise ValueError('Rating must be in 0.5 increments')
        return v
    
    class Config:
        orm_mode = True


class ReviewStatsSchema(BaseModel):
    product_id: int
    total_reviews: int
    average_rating: float
    rating_distribution: dict 