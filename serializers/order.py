# from pydantic import BaseModel
# from typing import Optional, List
# from datetime import datetime

# class OrderItemCreateSchema(BaseModel):
#     product_id: int
#     product_name: str
#     price: float
#     quantity: int

# class OrderItemSchema(BaseModel):
#     id: int
#     order_id: int
#     product_id: int
#     product_name: str
#     price: float
#     quantity: int

#     class Config:
#         orm_mode = True

# class OrderCreateSchema(BaseModel):
#     user_id: int
#     total_price: float
#     items: List[OrderItemCreateSchema]

# class OrderUpdateSchema(BaseModel):
#     status: Optional[str] = None

# class OrderSchema(BaseModel):
#     id: int
#     user_id: int
#     status: str
#     total_price: float
#     created_at: datetime
#     items: List[OrderItemSchema] = []

#     class Config:
#         orm_mode = True
