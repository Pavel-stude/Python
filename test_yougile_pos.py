import requests

token = "GJFTf4QOmKqg7sFWG6Gc8qFOn6K-MH5F875ASnkKVbEQrHtshHqbfFO3jKjyGBWG"
base_url = "https://ru.yougile.com/api-v2/"


def test_get_lisl_project_pos():
    #Позтитвная проверка на получение списка проектов
    my_heders = {'Authorization' : f'Bearer {token}',
              'Content-Type' : 'application/json'}
        
    resp = requests.get(base_url+"projects", headers=my_heders)
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0

def test_add_project_pos():
    #Позтитвная проверка на создание проекта
    my_heders = {'Authorization' : f'Bearer {token}',
        'Content-Type' : 'application/json'}
    
    my_data = {
    'title': 'YouGile Python',
    'users': {
        'c00dfd3a-901e-43a0-b668-20726a3ab6f4': 'admin'
    }
}
        
    resp = requests.post(base_url + "projects", 
                         headers=my_heders, json=my_data)
    body = resp.json()
    id_project = body["id"]

    assert resp.status_code == 201
    assert "id" in body
    assert id_project is not None


def test_update_project_pos():
    #Позтитвная проверка на изменение проекта
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
}

    create_data = {
        "title": "YouGile Python 1",
        "users": {
        "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
    }
}

    create_resp = requests.post(base_url + "projects", headers=my_headers, json=create_data)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    update_data = {
        "title": "Project YouGile",
        "users": {
        "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
    }
}

    update_resp = requests.put(
        base_url + f"projects/{project_id}",
        headers=my_headers,
        json=update_data
    )

    assert update_resp.status_code == 200

    get_resp = requests.get(
        base_url + f"projects/{project_id}",
        headers=my_headers
    )

    body = get_resp.json()
    assert body["title"] == "Project YouGile"