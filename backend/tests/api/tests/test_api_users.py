from tests.api.clients.users import UsersClient


def test_register_user(users_api_client: UsersClient, user_payload):
    response = users_api_client.register_user(**user_payload)

    assert response.json()["is_active"] == True
    assert response.json()["is_superuser"] == False


def test_get_user_by_id(created_user, users_authenticated_api_client: UsersClient):
    response = users_authenticated_api_client.get_user_by_id(created_user["id"])

    assert response.json()["id"] == created_user["id"]
    assert response.json()["is_active"] is True
