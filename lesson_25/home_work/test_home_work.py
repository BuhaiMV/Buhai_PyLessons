import lesson_25.home_work.infrastructure as infrastructure


def test_get_object():
    json, code = infrastructure.get_an_object(3)
    assert code == 200
    assert json == {
        "id": "3",
        "name": "Apple iPhone 12 Pro Max",
        "data": {
            "color": "Cloudy White",
            "capacity GB": 512
        }
    }


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
    json, code = infrastructure.create_an_object(test_data)
    assert code == 200
    assert type(json["id"]) == str
    assert type(json["name"]) == str
    assert type(json["data"]) == dict
    assert type(json["createdAt"]) == str


def test_update_an_object():
    test_data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    json1, code1 = infrastructure.create_an_object(test_data)
    test_data2 = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    json2, code2 = infrastructure.update_an_object(json1['id'], test_data2)
    assert code2 == 200
    assert type(json2["id"]) == str
    assert type(json2["name"]) == str
    assert type(json2["data"]) == dict
    assert type(json2["updatedAt"]) == str

def test_delete_an_object():
    test_data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    json1, code1 = infrastructure.create_an_object(test_data)
    json2, code2 = infrastructure.delete_an_object(json1['id'])
    assert code2 == 200
    assert type(json2["message"]) == str
