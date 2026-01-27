from models.booking import BookingModel
from datetime import datetime, timedelta

def create_bookings():
    now = datetime.utcnow()
    bookings = [
        BookingModel(
            booking_datetime=now + timedelta(days=2),
            status="pending",
            user_id=1,
            service_id=1
        ),
        BookingModel(
            booking_datetime=now + timedelta(days=3),
            status="approved",
            user_id=2,
            service_id=2
        ),
        BookingModel(
            booking_datetime=now + timedelta(days=5),
            status="rejected",
            user_id=3,
            service_id=3
        ),
        BookingModel(
            booking_datetime=now + timedelta(days=1),
            status="completed",
            user_id=4,
            service_id=4
        ),
        BookingModel(
            booking_datetime=now + timedelta(days=4),
            status="pending",
            user_id=5,
            service_id=5
        )
    ]
    return bookings

booking_list = create_bookings()
