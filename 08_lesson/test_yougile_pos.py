import requests
from conftest import BASE_URL, headers


def test_get_projects_list_positive():
    response = requests.get(BASE_URL + "projects", headers=headers)
    body = response.json()

    assert response.status_code == 200
    assert len(body) > 0


def test_add_project_positive():
    data = {
        'title': 'YouGile Python',
        'users': {
            'c00dfd3a-901e-43a0-b668-20726a3ab6f4': 'admin'
        }
    }

    response = requests.post(
        BASE_URL + "projects",
        headers=headers,
        json=data
    )
    body = response.json()
    project_id = body["id"]

    assert response.status_code == 201
    assert "id" in body
    assert project_id is not None


def test_update_project_positive():
    create_data = {
        "title": "YouGile Python 1",
        "users": {
            "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
        }
    }

    create_response = requests.post(
        BASE_URL + "projects",
        headers=headers,
        json=create_data
    )
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    update_data = {
        "title": "Project YouGile",
        "users": {
            "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
        }
    }

    update_response = requests.put(
        BASE_URL + f"projects/{project_id}",
        headers=headers,
        json=update_data
    )
    assert update_response.status_code == 200

    get_response = requests.get(
        BASE_URL + f"projects/{project_id}",
        headers=headers
    )
    body = get_response.json()
    assert body["title"] == "Project YouGile"