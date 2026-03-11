import requests
from conftest import BASE_URL, headers


def test_get_projects_no_auth():
    response = requests.get(BASE_URL + "projects")
    assert response.status_code == 401


def test_create_project_without_title():
    data = {
        "users": {
            "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
        }
    }

    response = requests.post(
        BASE_URL + "projects",
        headers=headers,
        json=data
    )

    assert response.status_code == 400


def test_update_project_wrong_id():
    update_data = {
        "title": "Project YouGile",
        "users": {
            "c00dfd3a-901e-43a0-b668-20726a3ab6f4": "admin"
        }
    }
    wrong_id = "123456"

    update_response = requests.put(
        BASE_URL + f"projects/{wrong_id}",
        headers=headers,
        json=update_data
    )

    assert update_response.status_code == 404