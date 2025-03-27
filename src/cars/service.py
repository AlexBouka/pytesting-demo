from typing import Optional
from pydantic import TypeAdapter

from .models import CarState
from .schemas import CarSchema
from .repository import CarCRUDRepository


class CarService:
    @classmethod
    def add(cls, car: CarSchema):
        car_dict = car.convert_to_dict_excluding_id()
        new_car = CarCRUDRepository.add(car_dict)
        return TypeAdapter(CarSchema).dump_python(new_car)

    @classmethod
    def get(cls, car_id):
        car = CarCRUDRepository.get(car_id)
        return TypeAdapter(CarSchema).dump_python(car)

    @classmethod
    def list_cars(
        cls,
        brand: Optional[str] = None,
        model: Optional[str] = None,
        state: Optional[CarState] = None,
    ):
        dict_args = {"brand": brand, "model": model, "state": state}
        filter_by = {k: v for k, v in dict_args.items() if v is not None}
        cars = CarCRUDRepository.list_cars(filter_by)
        return TypeAdapter(list[CarSchema]).dump_python(cars)

    @classmethod
    def update(cls, car_id: int, car: CarSchema):
        car_dict = car.convert_to_dict_excluding_id()
        CarCRUDRepository.update(car_id, car_dict)

    @classmethod
    def delete(cls, car_id: int):
        CarCRUDRepository.delete(car_id)

    @classmethod
    def delete_all(cls):
        CarCRUDRepository.delete_all()

    @classmethod
    def count(cls) -> int:
        return CarCRUDRepository.count()
