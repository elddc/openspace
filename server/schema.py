from typing import List, Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, SmallInteger
from sqlalchemy import ForeignKey
import uuid

class Base(DeclarativeBase):
    pass

class Building(Base):
    __tablename__="building"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(primary_key=True)
    address: Mapped[Optional[str]]
    location: Mapped[Optional[str]]
    capacity: Mapped[Optional[str]]
    busyness = mapped_column(SmallInteger)

    rooms: Mapped[List["Room"]] = relationship(back_populates="building")

    inputs: Mapped[List["Input"]] = relationship(back_populates="building")

    last_updated: Mapped[datetime.datetime]= mapped_column(oncreate=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, address={self.address!r}, location={self.location!r}, capacity={self.capacity!r}, busyness={self.busyness!r}, last_updated={self.last_updated!r})"

class Room(Base):
    __tablename__="room"
    building_id = mapped_column(ForeignKey("building.id"), primary_key=True)
    room_number: Mapped[int] = mapped_column(primary_key=True)
    busyness = mapped_column(SmallInteger)

    building: Mapped[Building] = relationship(back_populates="rooms")

    def __repr__(self) -> str:
        return f"Room(room_number={self.room_number!r}, busyness={self.busyness!r})"

class Input(Base):
    __tablename__="input"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    building_id = mapped_column(ForeignKey("building.id"))
    busyness = mapped_column(SmallInteger)

    building: Mapped[Building] = relationship(back_populates="inputs")

    time_created: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    def __repr__(self) -> str:
        return f"Input(id={self.id!r}, busyness={self.busyness!r})"








