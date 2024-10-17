import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
# from datetime import datetime
from ..db import db

class Continent(enum.Enum):
    AFRICA = "Africa"
    ANTARCTICA = "Antarctica"
    ASIA = "Asia"
    AUSTRALASIA = "Australasia"
    EUROPE = "Europe"
    NORTH_AMERICA = "North America"
    SOUTH_AMERICA = "South America"

class Trip(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    continent: Mapped[Continent]
    about: Mapped[Optional[str]]
    category: Mapped[str]
    weeks: Mapped[int]
    cost: Mapped[float]
    # available: Mapped[int]
    # sold: Mapped[int]
    # expires: Mapped[datetime]
    reservations: Mapped[list["Reservation"]] = relationship(back_populates="trip")

    def to_dict(self):
        trip_info = {
            "id": self.id,
            "name": self.name,
            "continent": self.continent,
            "category": self.category,
            "weeks": self.weeks,
            "cost": self.cost
        }

        if self.about:
            trip_info["about"] = self.about

        return trip_info
    
    @classmethod
    def from_dict(cls, trip_data):
        about = trip_data.get("about")

        new_trip = cls(
            name=trip_data["name"],
            continent=trip_data["continent"],
            about=about,
            category=trip_data["category"],
            weeks=trip_data["weeks"],
            cost=trip_data["cost"]
        )
        return new_trip