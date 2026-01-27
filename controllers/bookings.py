from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.booking import BookingModel
from models.service import ServiceModel
from models.user import UserModel
from serializers.booking import BookingSchema, BookingCreateSchema, BookingUpdateStatusSchema
from database import get_db
from typing import List
from dependencies.get_current_user import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/bookings", response_model=BookingSchema, status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    
    service = db.query(ServiceModel).filter(ServiceModel.id == booking.service_id).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    if not service.is_available:
        raise HTTPException(status_code=400, detail="Service is not available for booking")
    
    now = datetime.utcnow()

    if booking.booking_datetime <= now:
      raise HTTPException(status_code=400, detail="You cannot book a service in the past")

    new_booking = BookingModel(
        booking_datetime=booking.booking_datetime,
        service_id=booking.service_id,
        user_id=current_user.id,
        status="pending"
    )
    
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@router.get("/bookings/me", response_model=List[BookingSchema])
def get_my_bookings(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    bookings = db.query(BookingModel).filter(BookingModel.user_id == current_user.id).all()

    return bookings

@router.get("/bookings", response_model=List[BookingSchema])
def get_all_bookings(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized - Admin access required")
    
    bookings = db.query(BookingModel).filter(BookingModel.status == "pending").all()
    
    return bookings

@router.put("/bookings/{booking_id}/status", response_model=BookingSchema)
def update_booking_status(booking_id: int, status_update: BookingUpdateStatusSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized - Admin access required")
    
    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    booking.status = status_update.status
    db.commit()
    db.refresh(booking)
    return booking

@router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    if not current_user.is_admin and booking.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Unauthorized - You can only delete your own bookings")
    
    db.delete(booking)
    db.commit()
    return {"Message": f"Booking with ID {booking_id} was deleted!"}
