import pytest

from src.db import Base
from src.cars.schemas import CarSchema
from src.cars.service import CarService
from src.cars.models import CarState, Car


@pytest.fixture(scope="session", autouse=True)  # marks this fixture to run once
def prepare_database():
    print("Before DB creation")
    Base.metadata.drop_all()
    Base.metadata.create_all()
    print("After DB creation")


@pytest.fixture
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


@pytest.mark.usefixtures("remove_cars")
class TestCars:
    def test_count_cars(self, cars):
        for car in cars:
            CarService.add(car)

        assert CarService.count() == 3

    def test_list_cars(self, cars):
        for car in cars:
            CarService.add(car)

        all_cars = CarService.list_cars()
        for added_car in all_cars:
            assert car in cars
