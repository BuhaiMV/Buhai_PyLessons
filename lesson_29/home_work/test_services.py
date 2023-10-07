from lesson_29.home_work.services.db_service import DataBase
from lesson_29.home_work.services.endpoint_service import Endpoint

dataBase = DataBase()
endpoint = Endpoint()


def test_1():
    post_response = endpoint.post_request({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    get_response = endpoint.get_request(post_response['id'])
    add_data_in_db = dataBase.add_to_db({"data": get_response})
    get_data_from_db = dataBase.get_data_from_db(add_data_in_db.inserted_id)['data']
    print(get_response)
    print(get_data_from_db)
    assert get_response == get_data_from_db


def test_2():
    post_response = endpoint.post_request({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    add_data_to_db = dataBase.add_to_db({"data": post_response})

    put_response = endpoint.put_request(post_response['id'], {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    })
    get_response = endpoint.get_request(put_response['id'])
    dataBase.update_in_db(add_data_to_db.inserted_id, {"data": get_response})
    get_data_from_db = dataBase.get_data_from_db(add_data_to_db.inserted_id)['data']
    assert get_response == get_data_from_db


def test_3():
    add_data_to_db = dataBase.add_to_db({"data": {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }})
    get_data_from_db = dataBase.get_data_from_db(add_data_to_db.inserted_id)['data']
    post_response = endpoint.post_request(get_data_from_db['data'])

    dataBase.update_in_db(add_data_to_db.inserted_id, {"data": {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }})
    get_data_in_db = dataBase.get_data_from_db(add_data_to_db.inserted_id)['data']
    put_response = endpoint.put_request(post_response['id'], get_data_in_db)
    get_response = endpoint.get_request(put_response['id'])
    print(get_response)
    print(get_data_in_db)
    assert get_response == get_data_in_db
