import pytest
import time

from src.db_config import settings
from src.db import Base, sync_engine


# @pytest.fixture(scope="session", autouse=True)  # marks this fixture to run once
# def prepare_database():
#     print("Before DB creation")
#     Base.metadata.drop_all(sync_engine)
#     Base.metadata.create_all(sync_engine)
#     print("After DB creation")


@pytest.fixture(scope="session", autouse=True)  # marks this fixture to run once
def prepare_database():
    print(f"{settings.DATABASE_URL_psycopg}")
    assert settings.MODE == "TEST"
    Base.metadata.drop_all(sync_engine)    # Clear the DB
    Base.metadata.create_all(sync_engine)  # Create all tables
    yield                                  # Give control to pytest
    Base.metadata.drop_all(sync_engine)    # Drop the


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "firefox")
    )

    parser.addoption(
        "--run-slow",
        default="true",
        choices=("true", "false")
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


def test_browser(browser):
    print(browser)


@pytest.mark.skip(reason="Slow test")
def test_slow():
    time.sleep(3)


@pytest.mark.skipif('config.getoption("--run-slow") == "false"')
def test_very_slow():
    time.sleep(5)


def test_fast():
    pass
