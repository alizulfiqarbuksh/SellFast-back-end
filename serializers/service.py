from pydantic import BaseModel
from typing import Optional

class ServiceSchema(BaseModel):
    id: Optional[int] = None
    name: str
    description: str | None
    price: float
    duration_minutes: int
    is_available: bool
    image: Optional[str] = None

    class Config:
        orm_mode = True

class ServiceCreateSchema(BaseModel):
    name: str
    description: str | None = None
    price: float
    duration_minutes: int
    is_available: bool = True
    image: Optional[str] = None



class ServiceUpdateSchema(BaseModel):
    name: str
    description: str | None
    price: float
    duration_minutes: int
    is_available: bool
    image: Optional[str] = None
