import httpx
from typing import Any

BASE_URL = 'http://127.0.0.1:8000'


class APIClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.client = httpx.AsyncClient()

    async def close(self):
        await self.client.aclose()

    async def get_root(self) -> dict[str, Any]:
        response = await self.client.get(f'{self.base_url}/')
        response.raise_for_status()
        return response.json()

    async def create_user(self, user_data: dict[str, Any]) -> dict[str, Any]:
        response = await self.client.post(f'{self.base_url}/users/', json=user_data)
        response.raise_for_status()
        return response.json()

    async def create_pressure_measurements_for_user(
        self, user_id: int, pressure_data: dict[str, Any]
    ) -> dict[str, Any]:
        response = await self.client.post(
            f'{self.base_url}/users/{user_id}/pressure/', json=pressure_data
        )
        response.raise_for_status()
        return response.json()
