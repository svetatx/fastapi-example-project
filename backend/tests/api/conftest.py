import random
import string
import pytest

from tests.api.core.client import Client, Configuration
from tests.api.clients.users import UsersClient
from tests.api.clients.items import ItemsClient


base_url = "http://127.0.0.1:8000/api/v1"


@pytest.fixture
def api_client() -> Client:
    return Client(Configuration(base_url=base_url))


@pytest.fixture
def authenticated_api_client(auth_headers) -> Client:
    return Client(Configuration(base_url=base_url, headers=auth_headers))


@pytest.fixture
def users_api_client(api_client) -> UsersClient:
    return UsersClient(api_client)


@pytest.fixture
def users_authenticated_api_client(authenticated_api_client) -> UsersClient:
    return UsersClient(authenticated_api_client)


@pytest.fixture
def items_authenticated_api_client(authenticated_api_client) -> ItemsClient:
    return ItemsClient(authenticated_api_client)


def _rand_email(prefix="sveta"):
    return f"{prefix}{''.join(random.choices(string.digits, k=5))}@example.com"


@pytest.fixture
def user_payload():
    return {
        "email": _rand_email(),
        "password": "password123",
        "full_name": "qa_user",
    }


@pytest.fixture
def created_user(users_api_client: UsersClient, user_payload):
    yield users_api_client.register_user(**user_payload).json()


@pytest.fixture()
def auth_headers(created_user, api_client: Client, user_payload):
    response = api_client.post(
        url="/login/access-token",
        data={
            "username": user_payload["email"],
            "password": user_payload["password"],
        },
    )
    return {"Authorization": f"Bearer {response.json()['access_token']}"}


@pytest.fixture()
def item_payload():
    return {
        "title": f"demo_item_{''.join(random.choices(string.ascii_lowercase, k=5))}",
        "description": "created from API test",
    }
