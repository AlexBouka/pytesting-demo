from typing import Optional
from sqlalchemy import (
    Table, Column, Integer, Text, String, MetaData, ForeignKey,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    text, Enum
)
from enum import Enum as PyEnum
from sqlalchemy.orm import (
    Mapped, mapped_column, registry, relationship)

from ..db import Base


class CarState(str, PyEnum):
    NEW = "NEW",
    USED = "USED",
    SCRAPPED = "SCRAPPED"


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[Optional[str]] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(server_default=text("EXTRACT(YEAR FROM TIMEZONE('utc', now()))"))
    price: Mapped[int] = mapped_column(Integer)
    color: Mapped[str] = mapped_column(String(50))
    state: Mapped[CarState] = mapped_column(Enum(CarState, name="car_state", create_type=True), server_default=CarState.NEW.value)  # new, used, scrapped
