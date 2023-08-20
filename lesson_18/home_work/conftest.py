import pytest
from lesson_17.home_work.home_work_test.adapter_for_test import CsvManager


@pytest.fixture(scope='session')
def manager():
    yield CsvManager()

@pytest.fixture(scope='function')
def add_line():
    CsvManager().add_line({'first_name': 'Adam', 'last_name': "First", 'age': 45, 'gender': 'Male', 'salary': 60000})


@pytest.fixture(scope='function')
def delete_line():
    yield
    CsvManager().delete_line()


