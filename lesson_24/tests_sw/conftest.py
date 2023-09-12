import pytest
from lesson_24.infrastructure.people_service import PeopleService
from lesson_24.infrastructure.planet_service import PlanetService


@pytest.fixture()
def people_service():
    yield PeopleService()


@pytest.fixture()
def planetService():
    yield PlanetService()
