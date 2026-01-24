from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    is_available: bool

    class Config:
        orm_mode = True

class ProductCreateSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    is_available: bool = True

class ProductUpdateSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    is_available: bool

