import pytest

from src.cars.service import CarService


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
