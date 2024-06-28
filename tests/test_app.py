from http import HTTPStatus

from fastapi.testclient import TestClient

from ecommerce_fastapi.app import app

client = TestClient(app)


def test_read_root_returns_hello_world():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World 3'}
