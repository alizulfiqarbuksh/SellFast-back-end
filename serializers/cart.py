from pydantic import BaseModel
from typing import Optional, List

class CartItemCreateSchema(BaseModel):
    product_id: int
    quantity: int = 1

class CartItemUpdateSchema(BaseModel):
    quantity: int

class CartItemSchema(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class CartSchema(BaseModel):
    id: int
    user_id: int
    is_active: bool
    items: List[CartItemSchema] = []

    class Config:
        orm_mode = True
