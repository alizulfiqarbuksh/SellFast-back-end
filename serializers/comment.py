from pydantic import BaseModel

class CommentSchema(BaseModel):
  id: int
  content: str

  class Config:
    orm_mode = True


class CommentCreateSchema(BaseModel):
  content: str

  class Config:
    orm_mode = True

class CommentUpdateSchema(BaseModel):
  content: str

  class Config:
    orm_mode = True