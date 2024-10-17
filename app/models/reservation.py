from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from datetime import datetime
from ..db import db

class Reservation(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trip_id: Mapped[int] = mapped_column(ForeignKey("trip.id"))
    trip: Mapped["Trip"] = relationship(back_populates="reservations")
    name: Mapped[str]
    age: Mapped[Optional[int]]
    email: Mapped[str]

    def to_dict(self):
        booking_info = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "trip_id": self.trip_id
        }

        if self.age:
            booking_info["age"] = self.age

        return booking_info
    
    @classmethod
    def from_dict(cls, reservation_data):
        age = reservation_data.get("age")

        new_reservation = cls(
            name=reservation_data["name"],
            age=age,
            email=reservation_data["email"],
            trip_id=reservation_data["trip_id"]
        )
        return new_reservation