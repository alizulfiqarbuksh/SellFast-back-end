from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .service import ServiceSchema
from .user import UserSchema

class BookingSchema(BaseModel):
    id: Optional[int] = None
    booking_datetime: datetime
    status: str
    created_at: datetime

    user: UserSchema
    service: ServiceSchema

    class Config:
        orm_mode = True


class BookingCreateSchema(BaseModel):
    service_id: int
    booking_datetime: datetime



class BookingUpdateStatusSchema(BaseModel):
    status: str 

