import requests


def create_object():
    body = {
        "data": {
            "homework": "18",
            "fio": "BPV"
        },
        "id": 416,
        "name": "test api"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    print(response.status_code)
    print(response.json())


create_object()


def change_object_put():
    body = {
        "data": {
            "homework": "18",
            "fio": "BPV"
        },
        "id": 416,
        "name": "test api change_object"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put('http://167.172.172.115:52353/object/416', json=body, headers=headers)
    print(response.status_code)
    print(response.json())


change_object_put()


def change_object_patch():
    body = {"name": "test api change_object_patch"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch('http://167.172.172.115:52353/object/416', json=body, headers=headers)
    print(response.status_code)
    print(response.json())


change_object_patch()


def delete_object():
    response = requests.delete('http://167.172.172.115:52353/object/416')
    print(response.status_code)
    print(response.json())


delete_object()
