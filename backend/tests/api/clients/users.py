from tests.api.core.client import Client

class UsersClient:
    def __init__(self, client: Client):
        self.client = client

    def register_user(self, email: str, password: str, full_name: str):
        return self.client.post(
            url="/users/signup",
            json={"email": email, "password": password, "full_name": full_name},
        )

    def get_user_by_id(self, user_id: str):
        return self.client.get(
            url=f"/users/{user_id}",
        )
