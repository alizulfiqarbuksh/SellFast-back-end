# serializers/tea.py

from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema
from .user import UserSchema

# Whenever we send out json this will be our response
class TeaSchema(BaseModel):
  id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  in_stock: bool
  rating: int
  user: UserSchema
  comments: List[CommentSchema] = []

  class Config:
    orm_mode = True

# These two below are specifically for req.body
class CreateTeaSchema(BaseModel):
  name: str
  in_stock: bool
  rating: int

  class Config:
    orm_mode = True

class UpdateTeaSchema(BaseModel):
  name: str
  in_stock: bool
  rating: int

  class Config:
    orm_mode = True