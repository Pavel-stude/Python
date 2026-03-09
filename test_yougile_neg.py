import requests

token = "GJFTf4QOmKqg7sFWG6Gc8qFOn6K-MH5F875ASnkKVbEQrHtshHqbfFO3jKjyGBWG"
base_url = "https://ru.yougile.com/api-v2/"


def test_get_projects_no_auth():
    #Негативная проверка на получение списка проектов
        
    resp = requests.get(base_url+"projects")
    body = resp.json()

    assert resp.status_code == 401

def test_create_project_without_title():
    #Негативная проверка на создание проекта
    my_heders = {'Authorization' : f'Bearer {token}',
        'Content-Type' : 'application/json'}
    
    my_data = {
    'users': {
        'c00dfd3a-901e-43a0-b668-20726a3ab6f4': 'admin'
    }
}
        
    resp = requests.post(base_url + "projects", 
                         headers=my_heders, json=my_data)

    assert resp.status_code == 400


def test_update_project_wrong_id():
    #Негативная проверка на изменение проекта
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
}

    update_data = {
        "title": "Project YouGile",
        "users": {
        "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
    }
}
    wrong_id = "123456"

    update_resp = requests.put(
        base_url + f"projects/{wrong_id}",
        headers=my_headers,
        json=update_data
    )

    assert update_resp.status_code == 404

