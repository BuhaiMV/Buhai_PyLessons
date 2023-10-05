from lesson_29.home_work.services.db_service import DataBase
from lesson_29.home_work.services.endpoint_service import Endpoint

dataBase = DataBase()
endpoint = Endpoint()


def test_get_object():
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
    add_data_response = dataBase.add_to_db({"data": get_response})
    get_data_response = dataBase.get_data_from_db(add_data_response.inserted_id)['data']
    print(get_response)
    print(get_data_response)
    assert get_response == get_data_response


def test_get_object():
    post_response = endpoint.post_request({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    add_data_response = dataBase.add_to_db({"data": post_response})
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
    update_data_response = dataBase.update_in_db(add_data_response.inserted_id, {"data": get_response})
    get_data_response = dataBase.get_data_from_db(add_data_response.inserted_id)['data']
    print(get_response)
    print(get_data_response)
    assert get_response == get_data_response
