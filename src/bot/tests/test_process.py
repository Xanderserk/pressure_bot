import pytest
import httpx
from respx import MockRouter
from bot.service_layer.services import APIClient

BASE_URL = 'http://127.0.0.1:8000'


@pytest.fixture
def client():
    return APIClient(base_url=BASE_URL)


@pytest.mark.asyncio
async def test_get_root(client: APIClient, respx_mock: MockRouter):
    respx_mock.get(f'{BASE_URL}/').mock(
        return_value=httpx.Response(200, json={'message': 'Hello World'})
    )
    response = await client.get_root()
    assert response == {'message': 'Hello World'}


@pytest.mark.asyncio
async def test_create_user(client: APIClient, respx_mock: MockRouter):
    user_data = {'id': 123, 'telegram_nickname': 'testuser'}
    respx_mock.post(f'{BASE_URL}/users/').mock(
        return_value=httpx.Response(200, json={'id': 1, **user_data})
    )
    response = await client.create_user(user_data['id'], user_data['telegram_nickname'])
    assert response['telegram_nickname'] == user_data['telegram_nickname']
    assert 'id' in response


@pytest.mark.asyncio
async def test_create_pressure_measurements_for_user(
    client: APIClient, respx_mock: MockRouter
):
    pressure_data = [{'up': 120, 'down': 80, 'pulse': 60}]
    user_id = 1
    respx_mock.post(f'{BASE_URL}/users/{user_id}/pressure/').mock(
        return_value=httpx.Response(200, json=[{'id': 1, **pressure_data[0]}])
    )
    response = await client.create_pressure_measurements_for_user(
        user_id, pressure_data
    )
    assert response[0]['up'] == pressure_data[0]['up']
    assert response[0]['down'] == pressure_data[0]['down']
    assert 'id' in response[0]
