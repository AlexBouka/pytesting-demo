from typing import Optional
from pydantic import BaseModel, Field

from .models import CarState


class CarSchema(BaseModel):
    id: Optional[int] = Field(default=1)
    brand: str = Field(default="Undefined")
    model: str = Field(default="Undefined")
    year: int
    price: int = Field(default=0)
    color: str = Field(default="Undefined")
    state: CarState = Field(default=CarState.NEW)

    class Config:
        from_attributes = True

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        attributes = [
            "brand", "model", "year", "price", "color", "state"
        ]
        for attr in attributes:
            if getattr(self, attr) != getattr(other, attr):
                return False

        return True

    def convert_to_dict_excluding_id(self) -> dict:
        return self.model_dump(exclude={"id"})
