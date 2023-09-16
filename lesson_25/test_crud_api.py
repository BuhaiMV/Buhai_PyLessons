import lesson_25.infrastructure as infrastructure


def test_get_object():
    assert infrastructure.get_an_object(4).status_code == 200


def test_create_an_object():
    test_data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = infrastructure.create_an_object(test_data)
    get_response = infrastructure.get_an_object(response.json()["id"])
    assert get_response.status_code == 200
