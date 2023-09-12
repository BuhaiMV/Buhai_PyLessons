import pytest

from lesson_24.test_data.people_test_data import test_data, expected_data

ids = 'test_id, expect_id'


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def create_keys():
    listOfCort = []
    for i in range(len(test_data)):
        listOfCort.append((list(test_data.values())[i], list(expected_data.values())[i]))
    return listOfCort


@pytest.mark.parametrize(ids, create_keys())
def test_test_multipy_person(people_service, test_id, expect_id):
    response = people_service.get_people(test_id)
    assert response.json() == expect_id
