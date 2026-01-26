from pydantic import BaseModel, ConfigDict
from typing import List, Optional


# ---------- CART ITEM SCHEMAS ----------

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
    product_name: str
    price: float

    model_config = ConfigDict(from_attributes=True)


# ---------- CART SCHEMAS ----------

class CartCreateSchema(BaseModel):
    is_active: Optional[bool] = True


class CartUpdateSchema(BaseModel):
    is_active: Optional[bool] = None


class CartSchema(BaseModel):
    id: int
    user_id: int
    is_active: bool
    items: List[CartItemSchema] = []

    model_config = ConfigDict(from_attributes=True)
