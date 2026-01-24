from pydantic import BaseModel
from typing import Optional

class ProductCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    is_available: bool = True

class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    is_available: Optional[bool] = None

class ProductSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    is_available: bool

    class Config:
        orm_mode = True
