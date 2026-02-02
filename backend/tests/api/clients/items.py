from tests.api.core.client import Client

class ItemsClient:
    def __init__(self, client: Client):
        self.client = client

    def create_item(self, title: str, description: str):
        return self.client.post(
            url="/items/",
            json={"title": title, "description": description},
        )

    def get_item_by_id(self, item_id: int):
        return self.client.get(
            url=f"/items/{item_id}",
        )

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.client.get(
            url="/items/",
            params={"skip": skip, "limit": limit},
        )

    def update_item(self, item_id: int, title: str, description: str):
        return self.client.put(
            url=f"/items/{item_id}",
            json={"title": title, "description": description},
        )

    def delete_item(self, item_id: int):
        return self.client.delete(
            url=f"/items/{item_id}",
        )
