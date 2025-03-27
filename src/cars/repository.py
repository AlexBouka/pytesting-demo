from sqlalchemy import insert, select, update, delete, func

from ..db import Session
from .models import Car


class CarCRUDRepository:
    @classmethod
    def add(cls, values: dict):
        with Session() as session:
            stmt = insert(Car).values(**values).returning(Car)
            new_car = session.execute(stmt)
            session.commit()
            return new_car.scalar_one()

    @classmethod
    def get(cls, car_id: int):
        with Session() as session:
            query = select(Car).filter_by(id=car_id)
            car = session.execute(query)
            session.commit()
            return car.mappings().one()

    @classmethod
    def list_cars(cls, filter_by: dict):
        with Session() as session:
            query = select(Car).filter_by(**filter_by)
            cars = session.execute(query)
            session.commit()
            return cars.scalars().all()

    @classmethod
    def update(cls, car_id: int, values: dict):
        with Session() as session:
            query = update(Car).where(Car.id == car_id).values(**values)
            session.execute(query)
            session.commit()

    @classmethod
    def delete(cls, car_id: int):
        with Session() as session:
            query = delete(Car).where(Car.id == car_id)
            session.execute(query)
            session.commit()

    @classmethod
    def delete_all(cls):
        with Session() as session:
            query = delete(Car)
            session.execute(query)
            session.commit()

    @classmethod
    def count(cls):
        with Session() as session:
            query = select(func.count(Car.id))
            count = session.execute(query)
            session.commit()
            return count.scalar()
