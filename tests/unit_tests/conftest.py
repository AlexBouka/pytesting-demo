import pytest

from src.cars.schemas import CarSchema
from src.cars.service import CarService
from src.cars.models import CarState


@pytest.fixture(scope="function")
def cars():
    cars = [
        CarSchema(
            make="Toyota",
            model="Camry",
            year=2020,
            price=25000,
            color="black",
            state=CarState.USED,
        ),
        CarSchema(
            make="Honda",
            model="Civic",
            year=2018,
            price=18000,
            color="blue",
            state=CarState.USED,
        ),
        CarSchema(
            make="Cadillac",
            model="Deville",
            year=1987,
            price=0,
            color="black",
            state=CarState.SCRAPPED,
        )
    ]

    return cars


@pytest.fixture(scope="function")
def remove_cars():
    CarService.delete_all()
