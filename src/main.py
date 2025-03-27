import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from typing import Union

from src.db import Base, sync_engine

from src.cars.service import CarService
Base.metadata.drop_all(sync_engine)
Base.metadata.create_all(sync_engine)


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")

        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")

        return x + y


if __name__ == "__main__":
    calculator = Calculator()
