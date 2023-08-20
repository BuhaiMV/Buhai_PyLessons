import pytest
from lesson_18.code_for_testing import Human


@pytest.fixture(scope='session')
def human():
    print('\nsetup for test')
    yield Human('Joshua', 25, 'black')
    print('\nteardown for test')
